<template>
    <div>   
        <form @submit.prevent class="d-flex justify-content-center align-items-center mb-4">
            <div class="form-outline flex-fill">
                <input type="text" v-model="name" id="form2" class="form-control" placeholder="New Task.." />
            </div>
            <button type="submit" class="btn btn-info ms-2" @click="CreateTask">Add</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    data() {
        return {
            name:'',
            owner:'',
            created_on: ''
        }
    },
    props:{
        user_id:{
            type:Number,
            required: false
        }
    },
    methods: {
        CreateTask(){
            const formData ={
                name: this.name,
                owner: this.user_id,
                created_on: new Date()
            }
            axios
            .post('/api/create-task/', formData)
            .then(response => {
                this.name= ''
                console.log(response);
            })
            .catch(error => {
                    console.log(error);
            })
        }
    },
}
</script>
<style ></style>