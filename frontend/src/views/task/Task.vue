<template>
    <div>
        <h1>{{taskDetails.name}}</h1>
        <p>{{ taskDetails.caption }}</p>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'task',
    data() {
        return {
            taskDetails:{}
        }
    },
    methods: {
        async getTask(){
            const response = await axios.get(`/api/tasks/${this.$route.params.pk}/`)
            this.taskDetails = response.data
            console.log(this.taskDetails);
        }
    },
    mounted() {
        this.getTask()
    },
}
</script>
<style lang="">
    
</style>