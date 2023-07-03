<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <div v-if="IsAuthenticated === false">
      <router-link to="/signup">SignUp</router-link> |
      <router-link to="/login">Login</router-link>
    </div>
    <div v-if="IsAuthenticated === true">
      <router-link to="/shared-tasks">Shared Tasks</router-link> |
      <button @click="logout">Logout</button>
    </div>
    <div>
      {{ username }}
    </div>
  </nav>
  <router-view
  :user_id="user_id"
  :tasks="tasks"
  :username="username"
  @CreateTask="CreateTask"
  @checkToggle="checkToggle"
  @deleteTask="deleteTask"
  />
</template>

<script>

import axios from 'axios';

export default {
  name: "App",
  data() {
    return {
      IsAuthenticated: false,
      username: '',
      user_id: '',
      isLoading: false,
      tasks: [],
      filter: 'all'
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
    async test(){
      let r = await axios.get('/api/tasks/85/')
      console.log(r);
    }
  },
  mounted() {
    this.beforeCrete()
    this.getMe()
    this.getTasks()
    this.test()
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
