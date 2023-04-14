
<template>
  <h1 @click="getMe">Home</h1>
  <span></span>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: ''
    }
  },
  mounted() {
    this.getMe
  },
  methods: {
    getMe(e) {
      try {
        axios.get('api/v1/users/me/', {'csrf_token': localStorage.getItem('access')})
        .then(response => {
          // this.username = response
          console.log(response);
        })
      } catch (error) {
        alert(error.message)
      }
    }
  },
  
}
</script>