import test from "node:test";
import assert from "node:assert/strict";
import { createRegistry, Registry, definePlugin, loadCatalog } from "../sdk/registry.mjs";
import { MissingCredentialsError } from "../sdk/connector.mjs";

const mockFetch = (log, status = 200, body = { ok: true }) => async (url, init) => {
  log.push({ url: String(url), ...init });
  return { ok: status < 400, status, text: async () => JSON.stringify(body) };
};

test("every catalog manifest validates and has unique ids", async () => {
  const reg = await createRegistry({ env: {} });
  const ids = reg.list().map((c) => c.id);
  assert.equal(new Set(ids).size, ids.length);
  assert.ok(ids.length >= 30);
});

test("unconfigured connectors report missing vars and never call the network", async () => {
  const log = [];
  const reg = await createRegistry({ env: {}, fetch: mockFetch(log) });
  const h = await reg.get("openai").health();
  assert.equal(h.state, "unconfigured");
  assert.deepEqual(h.missing, ["OPENAI_API_KEY"]);
  assert.equal(log.length, 0);
});

test("auth schemes: bearer, header+prefix, basic, query, path template", async () => {
  const log = [];
  const env = { OPENAI_API_KEY: "sk-test-123456", DISCORD_BOT_TOKEN: "dtok-123456", TWILIO_ACCOUNT_SID: "ACabc123", TWILIO_AUTH_TOKEN: "tw-secret", SHODAN_API_KEY: "sh-123456", TELEGRAM_BOT_TOKEN: "123:ABCDEF" };
  const reg = await createRegistry({ env, fetch: mockFetch(log) });
  await reg.get("openai").health();
  await reg.get("discord").health();
  await reg.get("twilio").health();
  await reg.get("shodan").health();
  await reg.get("telegram").health();
  assert.equal(log[0].headers.Authorization, "Bearer sk-test-123456");
  assert.equal(log[1].headers.Authorization, "Bot dtok-123456");
  assert.equal(log[2].headers.Authorization, "Basic " + Buffer.from("ACabc123:tw-secret").toString("base64"));
  assert.ok(log[2].url.includes("/Accounts/ACabc123.json"));
  assert.ok(log[3].url.includes("key=sh-123456"));
  assert.ok(log[4].url.startsWith("https://api.telegram.org/bot123:ABCDEF/getMe"));
});

test("plugin actions run through the same authenticated pipeline", async () => {
  const log = [];
  const env = { TWILIO_ACCOUNT_SID: "ACabc123", TWILIO_AUTH_TOKEN: "tw-secret", TWILIO_FROM_NUMBER: "+15550001111" };
  const reg = await createRegistry({ env, fetch: mockFetch(log) });
  await reg.get("twilio").actions.sendSms({ to: "+15550002222", body: "hi" });
  assert.equal(log[0].method, "POST");
  assert.match(log[0].body, /To=%2B15550002222/);
});

test("secrets are redacted from network errors", async () => {
  const reg = await createRegistry({ env: { OPENAI_API_KEY: "sk-supersecret-999" }, fetch: async () => { throw new Error("boom sk-supersecret-999"); } });
  const h = await reg.get("openai").health();
  assert.equal(h.state, "error");
  assert.ok(!h.error.includes("sk-supersecret-999"));
});

test("runtime plugin: custom connector with hooks", async () => {
  const log = [];
  const catalog = await loadCatalog();
  const reg = new Registry(catalog, new Map(), { env: { ACME_KEY: "acme-123456" }, fetch: mockFetch(log, 200, { v: 1 }) });
  reg.register(
    { id: "acme", name: "Acme", category: "infra", baseUrl: "https://acme.test", auth: { type: "bearer", env: "ACME_KEY" }, env: [{ name: "ACME_KEY", required: true }] },
    definePlugin({ id: "acme", hooks: { beforeRequest: (c, req) => ({ ...req, headers: { ...req.headers, "X-Trace": "1" } }), afterResponse: (c, r) => ({ ...r, data: { wrapped: r.data } }) } }),
  );
  const r = await reg.get("acme").request("GET", "/x");
  assert.equal(log[0].headers["X-Trace"], "1");
  assert.deepEqual(r.data, { wrapped: { v: 1 } });
});

test("invalid manifests are rejected", () => {
  const reg = new Registry({ connectors: [] });
  assert.throws(() => reg.register({ id: "Bad_ID", name: "x", category: "ai", baseUrl: "https://x", env: [] }), /kebab-case/);
  assert.throws(() => reg.register({ id: "x", name: "x", category: "ai", baseUrl: "https://x", auth: { type: "bearer", env: "NOPE" }, env: [] }), /undeclared/);
});

test("missing template var throws MissingCredentialsError", async () => {
  const reg = await createRegistry({ env: {}, fetch: mockFetch([]) });
  await assert.rejects(() => reg.get("supabase").request("GET", "/rest/v1/"), MissingCredentialsError);
});
