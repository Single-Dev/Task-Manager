<template>
    <form @submit="login()">
        <h1>Login</h1>
        <div>
            <input type="string" placeholder="Username" v-model="username">
        </div>
        <div>
            <input type="password" placeholder="Password" v-model="password">
        </div>
        <div v-if="error">
            {{ error }}
        </div>
        <div v-if="success" id="success">
            Logged in Successfully
        </div>
        <button type="submit">Submit</button>
    </form>
</template>

<script>
import axios from 'axios'

export default {
        data: () => ({
            username: '',
            password: '',
            error: null,
            success: false
        }),
        methods: {
            login: async function () {
                const auth = { username: this.username, password: this.password };
                // Correct username is 'foo' and password is 'bar'
                const url = 'https://httpbin.org/basic-auth/foo/bar';
                this.success = false;
                this.error = null;

                try {
                    const res = await axios.get(url, { auth }).then(res => res.data);
                    this.success = true;
                } catch (err) {
                    this.error = err.message;
                }
            }
        },

    }
</script>