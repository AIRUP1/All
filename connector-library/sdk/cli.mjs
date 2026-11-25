#!/usr/bin/env node
import { writeFile, readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { createRegistry } from "./registry.mjs";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const [, , cmd, ...args] = process.argv;

// Minimal .env loader (no dependency). Real environment wins over the file.
async function loadDotenv() {
  try {
    for (const line of (await readFile(path.join(ROOT, ".env"), "utf8")).split("\n")) {
      const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*?)\s*(?:#.*)?$/);
      if (m && m[2] && !(m[1] in process.env)) process.env[m[1]] = m[2].replace(/^["']|["']$/g, "");
    }
  } catch { /* no .env */ }
}

const ICON = { healthy: "●", configured: "◐", rejected: "✖", error: "✖", unconfigured: "○" };
const help = `connector-library CLI
  list                       all connectors and whether credentials are present
  status                     list + live health probe for configured connectors
  test <id>                  health probe for one connector
  call <id> <METHOD> <path>  authenticated request (prints status + JSON body)
  env                        print a blank .env template
  build-ui                   regenerate catalog.js for the 3D viewer
`;

await loadDotenv();
const reg = await createRegistry();

switch (cmd) {
  case "list": {
    for (const c of reg.list()) {
      const miss = c.missing();
      console.log(`${miss.length ? ICON.unconfigured : ICON.configured} ${c.id.padEnd(14)} ${c.manifest.category.padEnd(10)} ${miss.length ? "missing: " + miss.join(", ") : "credentials present"}`);
    }
    break;
  }
  case "status": {
    for (const h of await reg.healthAll()) {
      console.log(`${ICON[h.state] ?? "?"} ${h.id.padEnd(14)} ${h.state}${h.status ? " " + h.status : ""}${h.ms ? ` ${h.ms}ms` : ""}${h.missing ? " (" + h.missing.join(", ") + ")" : ""}${h.error ? " " + h.error : ""}`);
    }
    break;
  }
  case "test": {
    console.log(JSON.stringify(await reg.get(args[0]).health(), null, 2));
    break;
  }
  case "call": {
    const [id, method, p] = args;
    if (!id || !method || !p) { console.error("usage: call <id> <METHOD> <path>"); process.exit(2); }
    const r = await reg.get(id).request(method, p);
    console.log(r.status, JSON.stringify(r.data, null, 2));
    break;
  }
  case "env": process.stdout.write(reg.envTemplate()); break;
  case "build-ui": {
    await writeFile(path.join(ROOT, "catalog.js"), `window.CONNECTOR_CATALOG = ${JSON.stringify(reg.catalog)};\n`);
    console.log("wrote catalog.js");
    break;
  }
  default: process.stdout.write(help); process.exit(cmd ? 2 : 0);
}
