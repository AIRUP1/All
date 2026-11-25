import { definePlugin } from "../sdk/registry.mjs";

export default definePlugin({
  id: "twilio",
  actions: {
    /** sendSms({ to, body, from? }) */
    async sendSms(c, { to, body, from = c.env.TWILIO_FROM_NUMBER }) {
      if (!to || !body || !from) throw new Error("sendSms needs to, body and from (or TWILIO_FROM_NUMBER)");
      return c.request("POST", "/Accounts/{TWILIO_ACCOUNT_SID}/Messages.json", { form: { To: to, From: from, Body: body } });
    },
  },
});
