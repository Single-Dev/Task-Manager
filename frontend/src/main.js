import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import axois from 'axios'

// import './assets/main.css'

const app = createApp(App)

app.use(router)

app.mount('#app')

// axois.defaults.baseURL = 'http://127.0.0.1:8000/'