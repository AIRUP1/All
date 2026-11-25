// Copy to plugins/<id>.mjs (files starting with "_" are ignored by the loader).
// The id must match a connector in catalog.json — or call registry.register(manifest, plugin)
// at runtime for connectors that are not in the catalog.
import { definePlugin } from "../sdk/registry.mjs";

export default definePlugin({
  id: "my-connector",
  hooks: {
    // Mutate/replace the outgoing request: { method, url: URL, headers, body }
    // beforeRequest: (c, req) => req,
    // Post-process { ok, status, data }
    // afterResponse: (c, res) => res,
    // Replace the default health probe. Return { state: "healthy" | "rejected" | "error", ... }
    // health: async (c) => ({ state: "healthy" }),
  },
  actions: {
    // Callable as registry.get("my-connector").actions.doThing({ ... })
    // doThing: (c, args) => c.request("GET", "/thing", { query: args }),
  },
});
