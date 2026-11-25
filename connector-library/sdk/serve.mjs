#!/usr/bin/env node
// Zero-dependency static server for the 3D viewer. Binds to localhost only.
import http from "node:http";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const PORT = Number(process.env.PORT ?? 4173);
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".mjs": "text/javascript; charset=utf-8", ".json": "application/json" };
// Only the viewer's public assets are served; sdk/, plugins/ and .env stay private.
const ALLOW = /^\/(index\.html|catalog\.js|vendor\/.+\.js)?$/;

http.createServer(async (req, res) => {
  const url = new URL(req.url, "http://localhost").pathname;
  if (!ALLOW.test(url)) { res.writeHead(404).end("Not found"); return; }
  const rel = url === "/" ? "index.html" : url.slice(1);
  try {
    const file = path.join(ROOT, rel);
    if (!file.startsWith(ROOT + path.sep)) throw new Error("traversal");
    res.writeHead(200, { "Content-Type": TYPES[path.extname(file)] ?? "application/octet-stream", "X-Content-Type-Options": "nosniff" });
    res.end(await readFile(file));
  } catch { res.writeHead(404).end("Not found"); }
}).listen(PORT, "127.0.0.1", () => console.log(`Connector Library → http://localhost:${PORT}`));
