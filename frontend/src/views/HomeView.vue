<template>
  <div class="home">
    {{ username }}
    <todo :user_id="user_id"/>
  </div>
</template>

<script>
import todo from '@/components/todo.vue'
import axios from 'axios'
export default {
  name: 'HomeView',
  data() {
    return {
      username: '',
      user_id:''
    }
  },
  components: {
    todo
  },
  methods:{
    getMe() {
        axios.get('/api/v1/users/me/',)
        .then(response => {
          this.username = response.data.username
          this.user_id = response.data.id
          console.log(response.data);
        })
        .catch(error=>{
          console.log(error);
        })
    },
  },
  mounted() {
    this.getMe()
  },
}
</script>
