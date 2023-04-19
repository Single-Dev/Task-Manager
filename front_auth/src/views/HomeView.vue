<template>
  <div class="home">
    <h1 @click="getMe">Home</h1>
  </div>
</template>

<script>
import axios from 'axios';
export default{
  data() {
    return {
      username:''
    }
  },
  methods:{
    getMe() {
        axios.get('api/v1/users/me/',)
        .then(response => {
          // this.username = response
          console.log(response.data);
        })
        .catch(error=>{
          console.log(error);
        })
    },
    
  },
  mounted() {
    this.getMe
  },
}
</script>
