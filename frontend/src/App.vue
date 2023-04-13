
<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/signup">Signup</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios'

export default {
  data(){
    return{
      state: {
        access: '',
        refresh: ''
      }
    }
  },
  methods: {
    initializeStore(state) {
      if (localStorage.getItem('access')) {
        state.access = localStorage.getItem('access')
      } else {
        state.access = ''
      }
    },
    setAccess(state, access) {
      state.access = access
    },
    beforeCreate() {
      if (this.access) {
        axios.defaults.headers.common['Authorization'] = "JWT" + access
      } else {
        axios.defaults.headers.common['Authorization'] = ''
      }
    },
    mounted() {
      this.initializeStore
      this.setAccess
    },
  }
}
</script>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
