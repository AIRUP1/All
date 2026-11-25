// Manifest-driven connector. Secrets are read from the environment at call time
// and are never stored on the object, logged, or returned in results.

const TEMPLATE = /\{([A-Z0-9_]+)\}/g;

export class MissingCredentialsError extends Error {
  constructor(id, missing) {
    super(`Connector "${id}" is missing env vars: ${missing.join(", ")}`);
    this.name = "MissingCredentialsError";
    this.missing = missing;
  }
}

export function redact(text, secrets) {
  let out = String(text);
  for (const s of secrets) if (s && s.length > 5) out = out.split(s).join("«redacted»");
  return out;
}

export class Connector {
  constructor(manifest, { env = process.env, fetch: fetchImpl = globalThis.fetch, plugin = null } = {}) {
    this.manifest = manifest;
    this.id = manifest.id;
    this.env = env;
    this.fetch = fetchImpl;
    this.plugin = plugin;
    this.actions = {};
    for (const [name, fn] of Object.entries(plugin?.actions ?? {})) {
      this.actions[name] = (args = {}) => fn(this, args);
    }
  }

  /** Env var names this connector needs (required ones only). */
  get requiredEnv() {
    return this.manifest.env.filter((e) => e.required).map((e) => e.name);
  }

  missing() {
    return this.requiredEnv.filter((n) => !this.env[n]);
  }

  isConfigured() {
    return this.missing().length === 0;
  }

  #secrets() {
    return this.manifest.env.map((e) => this.env[e.name]).filter(Boolean);
  }

  #fill(str) {
    return str.replace(TEMPLATE, (_, name) => {
      const v = this.env[name];
      if (!v) throw new MissingCredentialsError(this.id, [name]);
      return v;
    });
  }

  #authenticate(headers, url) {
    const a = this.manifest.auth ?? { type: "none" };
    const need = (n) => {
      const v = this.env[n];
      if (!v) throw new MissingCredentialsError(this.id, [n]);
      return v;
    };
    switch (a.type) {
      case "bearer": headers.Authorization = `Bearer ${need(a.env)}`; break;
      case "header": headers[a.name] = `${a.prefix ?? ""}${need(a.env)}`; break;
      case "basic":
        headers.Authorization = "Basic " + Buffer.from(`${need(a.userEnv)}:${need(a.passEnv)}`).toString("base64");
        break;
      case "query": url.searchParams.set(a.param, need(a.env)); break;
      case "none": break;
      default: throw new Error(`Unknown auth type "${a.type}" for ${this.id}`);
    }
  }

  /** Perform an authenticated request. `path` may contain {ENV_VAR} templates. */
  async request(method, path, { query, json, form, headers: extra } = {}) {
    const base = this.#fill(this.manifest.baseUrl).replace(/\/$/, "");
    const url = new URL(base + this.#fill(path.startsWith("/") ? path : "/" + path));
    for (const [k, v] of Object.entries(query ?? {})) url.searchParams.set(k, v);
    const headers = { ...(this.manifest.headers ?? {}), ...(extra ?? {}) };
    this.#authenticate(headers, url);

    let body;
    if (json !== undefined) { body = JSON.stringify(json); headers["Content-Type"] ??= "application/json"; }
    else if (form) { body = new URLSearchParams(form).toString(); headers["Content-Type"] ??= "application/x-www-form-urlencoded"; }

    let req = { method: method.toUpperCase(), url, headers, body };
    req = (await this.plugin?.hooks?.beforeRequest?.(this, req)) ?? req;

    let res;
    try {
      res = await this.fetch(req.url, { method: req.method, headers: req.headers, body: req.body });
    } catch (err) {
      throw new Error(redact(`${this.id}: network error: ${err.message}`, this.#secrets()));
    }
    const text = await res.text();
    let data = text;
    try { data = text ? JSON.parse(text) : null; } catch { /* keep text */ }
    let out = { ok: res.ok, status: res.status, data };
    out = (await this.plugin?.hooks?.afterResponse?.(this, out)) ?? out;
    return out;
  }

  /** Cheap authenticated probe. Never throws; returns a status record. */
  async health() {
    const started = Date.now();
    const missing = this.missing();
    if (missing.length) return { id: this.id, state: "unconfigured", missing };
    if (this.plugin?.hooks?.health) {
      try { return { id: this.id, ...(await this.plugin.hooks.health(this)) }; }
      catch (e) { return { id: this.id, state: "error", error: redact(e.message, this.#secrets()) }; }
    }
    const h = this.manifest.health;
    if (!h) return { id: this.id, state: "configured", note: "no health probe defined" };
    try {
      const r = await this.request(h.method, h.path);
      return { id: this.id, state: r.ok ? "healthy" : "rejected", status: r.status, ms: Date.now() - started };
    } catch (e) {
      return { id: this.id, state: "error", error: redact(e.message, this.#secrets()) };
    }
  }
}
