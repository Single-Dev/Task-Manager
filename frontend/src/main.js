import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import axios from 'axios'
import '@/assets/css/style.css'
import {jquery} from '@/assets/js/jquery.min.js'
// import {popper} from '@/assets/js/popper.js'
// import {bootstrap} from '@/assets/js/bootstrap.min.js'
import {main} from '@/assets/js/main.js'

axios.defaults.baseURL = 'http://127.0.0.1:8000'
createApp(App).use(store).use(router).mount('#app')

