import axios from "./axios";
import vuetify from "./vuetify";
import pinia from "@/store";
import router from "@/router";
import type { App } from "vue";

export function registerPlugins(app: App) {
  app
    .use(pinia)
    .use(axios, { baseUrl: "http://127.0.0.1:8000" })
    .use(vuetify)
    .use(router);
}
