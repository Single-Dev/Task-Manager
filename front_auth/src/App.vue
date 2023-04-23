<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/signup">SignUp</router-link> |
    <router-link to="/login">Login</router-link> 
    <button @click="beforeCreate">Click</button>
  </nav>
  <router-view />
</template>

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

<script>
import axios from 'axios';
export default {
  methods: {
    beforeCreate() {
      this.$store.commit('initializeStore')
      const access = this.$store.state.access
      console.log(access);
      if (access) {
        axios.defaults.headers.common['Authorization'] = "JWT" + access
      } else {
        axios.defaults.headers.common['Authorization'] = ''
        console.log('not access');
      }
    },
    // mounted() {
    //   this.beforeCreate
    // },
  }
}
</script>