import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import SharedTasks from '../views/SharedTasks.vue'
import Profile from '../views/Profile.vue'

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
    path: '/shared-tasks',
    name: 'SharedTasks',
    component: SharedTasks
  },{
    path: '/@:username',
    name: 'profile',
    component: Profile
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
