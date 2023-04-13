<template >
    <div class="container">
        <h1>Sign up</h1>
        <form @submit.prevent class="form w-50">
            <input type="text" v-model="username" placeholder="Username" class="form-control mb-3">
            <input type="email" v-model="email" placeholder="Email" class="form-control mb-3">
            <input type="password" v-model="password" placeholder="Password" class="form-control mb-3">
            <button type="button" class="btn btn-outline-dark w-100" @click="SubmitForm">Sign Up</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data(){
        return{
            username: '',
            email:'',
            password: '',
        }
    },
    methods:{
        SubmitForm(e){
            const FormData = {
                username : this.username,
                email: this.email,
                password: this.password,
            }
            try {
                const response = axios.post('api/v1/users/', FormData)
                console.log(response);
            } catch (error) {
                alert(error.message)
            }finally{
                this.$router.push('/')
                // this.username = ''
                // this.email = ''
                // this.password = ''
            }
        }
    }
}
</script>
<style>
    
</style>