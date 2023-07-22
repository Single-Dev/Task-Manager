<template>
  
    <SidebarMenu
    :menuTitle="menuTitle"
    :isExitButton="false"
    :profileName="'@' + username"
    :profileRole="''"
    :profileImg="'http://127.0.0.1:8000/media/profile/profile.jpg'"
    :isUsedVueRouter="true"
    :isLoggedIn="IsAuthenticated"
    :username="username"
    />
   <div>
    <router-view
    :user_id="user_id"
    :tasks="tasks"
    :username="username"
    @CreateTask="CreateTask"
    @checkToggle="checkToggle"
    @deleteTask="deleteTask"
    />
   </div>
</template>

<script>

import axios from 'axios'
import SidebarMenu from "@/components/navigations/SideBar.vue";
export default {
  name: "App",
  components: {SidebarMenu},
  data() {
    return {
      IsAuthenticated: false,
      username: '',
      user_id: '',
      isLoading: false,
      tasks: [],
      filter: 'all',
      // Side Bar
      menuTitle: "Task Manager",     
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
      this.getMe()
      this.getTasks()
    },
    async searchUsers(){
      const response = await axios.get('/api/users/?search=bekzodbek')
      console.log(response.data);
    },
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
    this.searchUsers()
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
