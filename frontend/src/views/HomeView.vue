<template>
  <div class="home">
    <todo :user_id="user_id" :tasks="tasks"/>
  </div>
</template>

<script>
import todo from '@/components/todo.vue'
export default {
  name: 'HomeView',
  components: {
    todo
  },
  props:{
    user_id:{
      type:Number,
      required: true
    },
    tasks:{
      type: Array,
      required: true
    },
  }
}
</script>
