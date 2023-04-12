import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import About from '../views/AboutView.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: About
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
    }
  ]
})

export default router
