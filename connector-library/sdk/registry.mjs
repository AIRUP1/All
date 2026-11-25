import { readFile, readdir } from "node:fs/promises";
import { fileURLToPath, pathToFileURL } from "node:url";
import path from "node:path";
import { Connector } from "./connector.mjs";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

/** Identity helper that gives plugin authors a typed-looking entry point. */
export function definePlugin(plugin) {
  if (!plugin?.id) throw new Error("definePlugin: `id` is required");
  return plugin;
}

export class Registry {
  #connectors = new Map();

  #opts;

  constructor(catalog, plugins = new Map(), opts = {}) {
    this.catalog = catalog;
    this.#opts = opts;
    for (const m of catalog.connectors) this.register(m, plugins.get(m.id));
  }

  /** Add or replace a connector at runtime (this is the plugin extension point). */
  register(manifest, plugin, opts = {}) {
    validateManifest(manifest);
    const c = new Connector(manifest, { ...this.#opts, ...opts, plugin: plugin ?? null });
    this.#connectors.set(manifest.id, c);
    return c;
  }

  get(id) {
    const c = this.#connectors.get(id);
    if (!c) throw new Error(`Unknown connector "${id}". Known: ${[...this.#connectors.keys()].join(", ")}`);
    return c;
  }

  list() { return [...this.#connectors.values()]; }

  /** Health of every connector (concurrent, never throws). */
  async healthAll() {
    return Promise.all(this.list().map((c) => c.health()));
  }

  /** .env template for every connector, values blank. */
  envTemplate() {
    return this.list().map((c) => {
      const lines = c.manifest.env.map((e) => `${e.name}=${e.required ? "" : "   # optional"}`.trimEnd());
      return `# ${c.manifest.name}\n${lines.join("\n")}`;
    }).join("\n\n") + "\n";
  }
}

export function validateManifest(m) {
  const bad = (msg) => { throw new Error(`Invalid manifest "${m?.id ?? "?"}": ${msg}`); };
  if (!/^[a-z0-9-]+$/.test(m?.id ?? "")) bad("id must be kebab-case");
  for (const k of ["name", "category", "baseUrl"]) if (!m[k]) bad(`missing ${k}`);
  if (!Array.isArray(m.env)) bad("env must be an array");
  const names = new Set(m.env.map((e) => e.name));
  const a = m.auth ?? { type: "none" };
  for (const n of [a.env, a.userEnv, a.passEnv].filter(Boolean)) if (!names.has(n)) bad(`auth references undeclared env var ${n}`);
  for (const [, n] of m.baseUrl.matchAll(/\{([A-Z0-9_]+)\}/g)) if (!names.has(n)) bad(`baseUrl references undeclared env var ${n}`);
  for (const [, n] of (m.health?.path ?? "").matchAll(/\{([A-Z0-9_]+)\}/g)) if (!names.has(n)) bad(`health.path references undeclared env var ${n}`);
}

/** Insert or replace a manifest (by id) in a catalog object. Returns "added" | "updated". */
export function upsertManifest(catalog, manifest) {
  validateManifest(manifest);
  if (manifest.category && !catalog.categories?.[manifest.category]) {
    throw new Error(`Invalid manifest "${manifest.id}": unknown category "${manifest.category}"`);
  }
  const i = catalog.connectors.findIndex((c) => c.id === manifest.id);
  if (i >= 0) { catalog.connectors[i] = manifest; return "updated"; }
  catalog.connectors.push(manifest); return "added";
}

export async function loadCatalog(file = path.join(ROOT, "catalog.json")) {
  return JSON.parse(await readFile(file, "utf8"));
}

/** Import every plugins/*.mjs (default export = definePlugin(...)). */
export async function loadPlugins(dir = path.join(ROOT, "plugins")) {
  const plugins = new Map();
  let files = [];
  try { files = (await readdir(dir)).filter((f) => f.endsWith(".mjs") && !f.startsWith("_")); } catch { /* none */ }
  for (const f of files) {
    const mod = await import(pathToFileURL(path.join(dir, f)).href);
    const p = mod.default;
    if (!p?.id) throw new Error(`plugins/${f}: default export must be definePlugin({ id, ... })`);
    plugins.set(p.id, p);
  }
  return plugins;
}

export async function createRegistry(opts = {}) {
  const [catalog, plugins] = await Promise.all([loadCatalog(opts.catalogFile), loadPlugins(opts.pluginsDir)]);
  return new Registry(catalog, plugins, { env: opts.env, fetch: opts.fetch });
}
