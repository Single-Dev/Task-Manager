<template >
    <div>
        <h1>SignUp</h1>
        <form @submit.prevent>
            <input type="text" name="username" v-model="username">
            <input type="email" name="email" v-model="email">
            <input type="password" name="username" v-model="password">
            <button type="submit" @click="submitForm">Submit</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name: 'SignUp',
    data() {
        return {
            email: '',
            username: '',
            password: '',
        }
    },
    methods: {
        submitForm(e) {
            const formData = {
                email: this.email,
                username: this.username,
                password: this.password,
            }
            axios
                .post('api/v1/users/', formData)
                .then(response => {
                    this.$router.push('/login')
                    console.log(response);
                })
                .catch(error => {
                    console.log(error);
                })
        }
    }
}
</script>
<style ></style>