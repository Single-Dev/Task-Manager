<template>
  <nav>
    <router-link to="/">Home</router-link>
    <div v-if="IsAuthenticated === false">
      <router-link to="/signup">SignUp</router-link> |
      <router-link to="/login">Login</router-link>
    </div>
    <button v-if="IsAuthenticated === true" @click="logout">Logout</button>
  </nav>
  <router-view />
</template>

<script>

import axios from 'axios';

export default {
  name: "App",
  data() {
    return {
      IsAuthenticated: false,
    }
  },
  methods: {
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
    async logout(){
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/v1/token/logout/')
        localStorage.removeItem('token')
        axios.defaults.headers.common['Authorization'] = ''
        this.$router.push('/')
        console.log(response);
      } catch (error) {
        alert(error.message)
      }
    }
  },
  mounted() {
    this.beforeCrete()
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
