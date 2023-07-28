<template>
    <SidebarMenu
    :profileName="'@' + username"
    :profileImg="''"
    :isLoggedIn="IsAuthenticated"
    :username="username"
    @onExit="logout"
    />
   <div>
   
    <router-view
    :isLoading="isLoading"
    :user_id="user_id"
    :tasks="tasks"
    :username="username"
    @CreateTask="CreateTask"
    @checkToggle="checkToggle"
    @deleteTask="deleteTask"
    @Login="Login"
    @Signup="Signup"
    />
   </div>
</template>

<script>

import axios from 'axios'
import SidebarMenu from "@/components/navigations/SideBar.vue";
import loader from '@/components/ui-components/Loader.vue'
export default {
  name: "App",
  components: {SidebarMenu, loader},
  data() {
    return {
      IsAuthenticated: false,
      username: '',
      user_id: '',
      isLoading: false,
      tasks: [],
    }
  },
  methods: {
    async getMe() {
      axios.get('/api/v1/users/me/')
        .then(response => {
          this.username = response.data.username
          this.user_id = response.data.id
        })
        .catch(error => {
          this.$router.push('/login')
        })
    },
    async getTasks() {
      try {
        this.isLoading = true
        const response = await axios.get('/api/tasks/')
        const newArr = response.data.map(item => ({
          id: item.id,
          name: item.name,
          caption: item.caption,
          done: item.done,
          created_on: item.created_on,
          reminder: item.reminder,
          owner: item.owner
        }))
        this.tasks = newArr
      } catch (error) {
        console.log(error.message)
      } finally {
        this.isLoading = false
      }
    },
    beforeCrete() {
      this.$store.commit('initializeStore')
      const token = this.$store.state.token
      this.IsAuthenticated = this.$store.state.IsAuthenticated
      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ''
      }
    },
    async Signup(email, username, password){
      const formData = {
                email: email,
                username: username.toLowerCase(), // Lowercase
                password: password,
            }
      try {
        const response = await axios.post('/api/v1/users/', formData)
        this.$router.push('/login')
      } catch (error) {
        alert(error.message)
      }
    },
    async Login(username, password){
      const formData = {username: username, password: password}
      try {
        const response = await axios.post('/api/v1/token/login/', formData)
        
        const token = response.data.auth_token

        this.$store.commit('setToken', token)

        axios.defaults.headers.common['Authorization'] = "Token " + token

        localStorage.setItem('token', token)
        this.IsAuthenticated = true
        this.getTasks()
        this.getMe()
        this.$router.push('/')
      } catch (error) {
        alert(error.message)
      }
    },
    // Search User
    async searchUsers(){
      try {
        const response = await axios.get('/api/users/?search=bekzodbek')
      } catch (error) {
        console.log(error.message);
      }
    },
    // LogOut
    async logout() {
      try {
        await axios.post('/api/v1/token/logout/')
        localStorage.removeItem('token')
        axios.defaults.headers.common['Authorization'] = ''
      } catch (error) {
        alert(error.message)
      } finally {
        this.beforeCrete()
      }
    },
    async CreateTask(item) {
      try {
        const response = await axios.post('/api/create-task/', item)
        this.tasks.push(response.data)
      } catch (error) {
        alert(error.message)
      }
    },
    async checkToggle(item) {
      item.done = !item.done
      try {
        await axios.post(`/api/updata/${item.id}/`, item)
      } catch (error) {
        alert(error.message)
      }
    },
    async deleteTask(item) {
      try {
        await axios.delete(`/api/delete/${item.id}/`, item)
        this.tasks = this.tasks.filter(c => c.id != item.id)
      } catch (error) {
        alert(error.message)
      }
    },
  },
  mounted() {
    this.beforeCrete()
    this.getMe()
    this.getTasks()
  },
}

</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
