import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Login from '../views/Login.vue'
import LoginSimple from '../views/LoginSimple.vue'
import Signup from '../views/Signup.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/signup',
    name:'signup',
    component:Signup
  },
  {
    path:'/login',
    name:"login",
    component: Login
  },
  {
    path:'/login-simple',
    name:"login",
    component: LoginSimple
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
