import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import axios from 'axios'
import '@/assets/css/style.css'
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
Vue.component('vue-sidebar-menu-akahon', VueSidebarMenuAkahon);


axios.defaults.baseURL = 'http://127.0.0.1:8000'
createApp(App).use(store).use(router).mount('#app')

