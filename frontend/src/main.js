import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import axios from 'axios'
import '@/assets/css/style.css'
// import '@/assets/js/jquery.min.js'
// import '@/assets/js/bootstrap.min.js'
// import '@/assets/js/main.js'
// import '@/assets/js/popper.js';
// global.jQuery = require('jquery');
// require('bootstrap');


axios.defaults.baseURL = 'http://127.0.0.1:8000'
createApp(App).use(store).use(router).mount('#app')

