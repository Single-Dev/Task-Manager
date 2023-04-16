<template >
    <div class="container">
        <h1>Login</h1>
        <form @submit.prevent class="form w-50">
            <input type="text" v-model="username" placeholder="Username" class="form-control mb-3">
            <input type="password" v-model="password" placeholder="Password" class="form-control mb-3">
            <button type="button" class="btn btn-outline-dark w-100" @click="SubmitForm">login</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    data(){
        return{
            username: '',
            password: '',
        }
    },
    methods:{
        SubmitForm(){
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem("access")

            const FormData = {
                username : this.username,
                email: this.email,
                password: this.password,
            }
            try {
                axios.post('api/v1/jwt/create/', FormData)
                .then(response => {
                    const access =  response.data.access
                    // console.log(access);
                    this.$store.commit('setAccess', access)

                    axios.defaults.headers.common['Authorization'] = 'JWT' + access

                    localStorage.setItem('access', access)
                    
                })
            } catch (error) {
                alert(error.message)
            } finally{
                this.$router.push('/')
            }

        }
    }
}
</script>
<style>
    
</style>