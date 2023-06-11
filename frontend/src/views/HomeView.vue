<template>
  <div class="home">
    {{ username }}
    <todo :user_id="user_id" :tasks="tasks"/>
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
      user_id: '',
      isLoading: false,
      tasks: []
    }
  },
  components: {
    todo
  },
  methods: {
    getMe() {
      axios.get('/api/v1/users/me/',)
        .then(response => {
          this.username = response.data.username
          this.user_id = response.data.id
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        })
    },
    async getTasks() {
      try {
        this.isLoading = true
        const response = await axios.get('/api/tasks/',)
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
        console.log(this.tasks);
      } catch (error) {
        alert(error.message)
      } finally {
        this.isLoading = false
      }
    },
  },
  mounted() {
    this.getMe()
    this.getTasks()
  },
}
</script>
