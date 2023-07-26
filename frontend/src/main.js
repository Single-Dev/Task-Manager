import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import axios from 'axios'
import '@/assets/css/style.css'
import uiComponents from '@/components/ui-components/index.js'
axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)
app.use(store).use(router)
uiComponents.map(component =>{
    app.component(component.name, component)
})
app.mount('#app')

