import { definePlugin } from "../sdk/registry.mjs";

export default definePlugin({
  id: "resend",
  actions: {
    /** sendEmail({ from, to, subject, html }) */
    sendEmail: (c, { from, to, subject, html }) =>
      c.request("POST", "/emails", { json: { from, to: [].concat(to), subject, html } }),
  },
});
