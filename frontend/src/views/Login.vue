<template >
    <div>
        <h1>Login</h1>
        <form @submit.prevent>
            <input type="text" name="username" v-model="username">
            <input type="password" name="username" v-model="password">
            <button type="submit" @click="submitForm">Submit</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        submitForm(e) {
            const formData = {
                username: this.username,
                password: this.password,
            }
            axios
                .post('/api/v1/token/login/', formData)
                .then(response => {
                    console.log(response);

                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common['Authorization'] = "Token " +token
                    
                    localStorage.setItem('token', token)
                })
                .catch(error => {
                    console.log(error);
                })
        }
    }
}
</script>
<style ></style>