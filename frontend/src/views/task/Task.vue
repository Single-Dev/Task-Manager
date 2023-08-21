<template>
    <div class="vh-100 gradient-custom d-flex justify-content-center align-items-center">
            <div class="card-box p-3">
                <div>
                    <h4>{{ taskDetails.name }}</h4>
                    <div class="d-flex justify-content-between align-items-center p-3">
                        <h6>Id: {{ taskDetails.id }}</h6>
                        <p>status: {{ taskDetails.done }}</p>
                        <p>created on: {{ taskDetails.created_on }}</p>
                    </div>
                    <div class="caption text-left">
                        <p>{{ taskDetails.caption }}</p>
                    </div>
                </div>
            </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'task',
    data() {
        return {
            taskDetails: {}
        }
    },
    methods: {
        async getTask() {
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
<style scoped>
.gradient-custom {
    background-image: linear-gradient(-20deg, #ff2846 0%, #6944ff 100%);
}
.card-box{
    width: 580px;
    padding: 10px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0px 8px 60px -10px rgba(13, 28, 39, 0.6);
}

.caption{
    background-color: #f4f6f7;
    padding:20px;
}

</style>