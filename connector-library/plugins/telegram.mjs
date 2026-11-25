import { definePlugin } from "../sdk/registry.mjs";

export default definePlugin({
  id: "telegram",
  actions: {
    /** sendMessage({ chatId, text }) */
    sendMessage: (c, { chatId, text }) => c.request("POST", "/sendMessage", { json: { chat_id: chatId, text } }),
  },
});
