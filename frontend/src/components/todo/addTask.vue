<template>
    <div>   
        <form @submit.prevent class="d-flex justify-content-center align-items-center mb-4">
            <div class="form-outline flex-fill">
                <input type="text" v-model="name" id="form2" class="form-control" placeholder="New Task.." />
            </div>
            <button type="submit" class="btn btn-outline-primary ms-2" @click="CreateTask">
                Add
                <i class="fas fa-plus"></i>
            </button>
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
            const newTask ={
                name: this.name,
                owner: this.user_id,
                created_on: new Date()
            }
            if(this.name == ''){
                alert('Nimadir Xato ketdi')                
            }else{
                this.$emit("CreateTask", newTask)
                this.name = ''
            }
        }
    },
}
</script>
<style ></style>