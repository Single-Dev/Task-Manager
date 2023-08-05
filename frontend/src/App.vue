<template>
  <SidebarMenu
  :isLoggedIn="IsAuthenticated"
  :username="username"
  @UpdateTerm="onTermHandler"
  @onExit="logout"/>
  <div>
    <router-view
    :isLoading="isLoading"
    :user_id="user_id"
    :tasks="tasks"
    :username="username"
    :users="users"
    :getting_users="getting_users"
    :apiBaseURL="apiBaseURL"
    @CreateTask="CreateTask"
    @checkToggle="checkToggle"
    @deleteTask="deleteTask"
    @Login="Login"
    @Signup="Signup" />
  </div>
</template>

<script>

import axios from 'axios'
import SidebarMenu from "@/components/navigations/SideBar.vue";

export default {
  name: "App",
  components: { SidebarMenu },
  data() {
    return {
      IsAuthenticated: false,
      username: '',
      user_id: '',
      isLoading: false,
      apiBaseURL: axios.defaults.baseURL,
      tasks: [],
      term: '',
      users:[],
      getting_users: false
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
    async Signup(email, username, password) {
      const formData = {
        email: email,
        username: username.toLowerCase(),
        password: password,
      }
      try {
        await axios.post('/api/v1/users/', formData)
        this.$router.push('/login')
      } catch (error) {
        alert(error.message)
      }
    },
    async Login(username, password) {
      const formData = { username: username, password: password }
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
    async searchForUser() {
      try {
        this.getting_users = true
        const response = await axios.get(`/api/users/?search=${this.term}`)
        const profiles = await axios.get('/api/profiles/')
        response.data.forEach(e =>{
          const profile = profiles.data.find(profile => profile.user === e.id);
          const user = {
              id: e.id,
              first_name: e.first_name,
              last_name: e.last_name,
              email: e.email,
              username: e.username,
              profile_photo: profile.profile_photo,
              bio: profile.bio
          }
          this.users.push(user)
      })
      } catch (error) {
        console.log(error.message);
      } finally {
        this.getting_users = false
      }
     
    },
    onTermHandler(term) {
      this.term = term
      const currentPath = this.$router.currentRoute._rawValue.href
      if(this.term.length > 3){
        this.searchForUser()
      }
      if(currentPath != '/result' && this.term.length > 3){
        this.$router.push('/result')
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
        this.getTasks()
        this.IsAuthenticated = false
        this.$router.push('/login')
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

<style >
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body {
  transition: all 0.5s ease;
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
