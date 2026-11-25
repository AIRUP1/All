# Connector Library

A plugin-based connector library for the services Air Agents uses (AI, voice, messaging, CRM, scraping, infra), with a **3D interactive catalog**.

```
connector-library/
├── catalog.json        # source of truth: one manifest per connector (no secrets)
├── catalog.js          # generated from catalog.json for the viewer (npm run build:ui)
├── index.html          # 3D viewer (three.js, vendored in vendor/ — works offline)
├── sdk/
│   ├── connector.mjs   # manifest-driven HTTP connector (auth, templating, redaction)
│   ├── registry.mjs    # Registry, definePlugin(), plugin loader, manifest validation
│   ├── cli.mjs         # list / status / test / call / env / build-ui
│   └── serve.mjs       # localhost static server for the viewer
├── plugins/            # drop-in plugins (twilio, telegram, resend + _template.mjs)
└── test/               # node:test suite (mock fetch, no network)
```

## Quick start

```bash
cp .env.example .env      # fill in only what you use; .env is git-ignored
npm run list              # which connectors have credentials
npm run status            # live health probe of configured connectors
npm run ui                # 3D viewer on http://localhost:4173
npm test
```

## Security model

- **No credential is ever stored in the catalog, the viewer, or the repo.** A manifest only names the env var (`"env": "OPENAI_API_KEY"`).
- Secrets are read from `process.env` at call time, never kept on the connector object, and are scrubbed from error messages.
- The viewer's "marked configured" switch is a `localStorage` flag in your browser — it holds no secrets.
- `serve.mjs` binds to `127.0.0.1` and only serves `index.html`, `catalog.js` and `vendor/*.js`.

## Register or update a connector (from the viewer)

Click **＋ Register connector** (or **Update this connector** on any tile). The form takes the service's base URL, auth style, health check and capabilities. It accepts only env var **names** — pasting something that looks like a key is rejected. Saving creates a *local draft* (browser only, shown in 3D with a badge). To make it permanent, download the JSON and run:

```bash
node sdk/cli.mjs register acme-crm.json   # adds or updates catalog.json + catalog.js
```

## Add a connector (by hand)

**Declarative** — append to `catalog.json`, then `npm run build:ui`:

```json
{ "id": "acme", "name": "Acme", "category": "infra", "description": "…",
  "baseUrl": "https://api.acme.com/v1",
  "auth": { "type": "bearer", "env": "ACME_API_KEY" },
  "env": [{ "name": "ACME_API_KEY", "required": true }],
  "health": { "method": "GET", "path": "/me" },
  "capabilities": ["things"] }
```

Auth types: `bearer`, `header` (`name`, optional `prefix`), `basic` (`userEnv`/`passEnv`), `query` (`param`), `none`.
`{ENV_VAR}` placeholders are allowed in `baseUrl` and paths (e.g. Telegram's `/bot{TELEGRAM_BOT_TOKEN}`).

**Plugin** — add `plugins/<id>.mjs` (see `plugins/_template.mjs`) to get `hooks` (`beforeRequest`, `afterResponse`, `health`) and custom `actions`:

```js
import { createRegistry } from "./sdk/registry.mjs";
const reg = await createRegistry();
await reg.get("twilio").actions.sendSms({ to: "+1555…", body: "hello" });
```

Connectors can also be registered at runtime: `reg.register(manifest, definePlugin({...}))`.

## Notes

- Base URLs and health endpoints are best-effort from each vendor's public docs; connectors without a `health` block (Perplexity, Manus, Zillow, …) report `configured` instead of probing. Verify before relying on them.
- Webex, Retell and other OAuth/webhook flows are modeled with their static tokens only; token refresh is not implemented.
