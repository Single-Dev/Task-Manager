import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import SharredTasks from '../views/SharredTasks.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },{
    path: '/signup',
    name: 'SignuUp',
    component: SignUp
  },{
    path: '/login',
    name: 'Login',
    component: Login
  },{
    path: '/sharred-tasks',
    name: 'SharredTasks',
    component: SharredTasks
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
