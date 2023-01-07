import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { registerSW } from "virtual:pwa-register";

const app = createApp(App)

app.use(router)

app.mount('#app')

import loaderUrl from '@/assets/loader.mp4'
var preloadLink = document.createElement("link")
preloadLink.href = loaderUrl
preloadLink.rel = "prefetch"
// preloadLink.as = "video"
document.head.appendChild(preloadLink);

if ("serviceWorker" in navigator) {
    registerSW({ immediate: true });
}