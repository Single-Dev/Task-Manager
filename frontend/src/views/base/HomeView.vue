<template>
  <div class="home">
    <todo
    :user_id="user_id"
    :tasks="tasks"
    :isLoading="isLoading"
    @CreateTask="$emit('CreateTask', $event)"
    @checkToggle="$emit('checkToggle', $event)"
    @deleteTask="$emit('deleteTask', $event)"
    />
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
    isLoading:{
      type: Boolean,
      required: true
    },
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
