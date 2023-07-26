<template >
    <form @submit.prevent class="w-75 text-center p-5">
        <div class="p-5 card mx-4 mx-md-5">
            <h2>Login</h2>
            <!-- Email input -->
            <div class="form-outline mb-4">
                <input type="text" id="form2Example1" class="form-control" v-model="username" />
                <label class="form-label" for="form2Example1">Username</label>
            </div>

            <!-- Password input -->
            <div class="form-outline mb-4">
                <input type="password" id="form2Example2" class="form-control" v-model="password" />
                <label class="form-label" for="form2Example2">Password</label>
            </div>

            <!-- 2 column grid layout for inline styling -->
            <div class="row mb-4">
                <div class="col d-flex justify-content-center">
                    <!-- Checkbox -->
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" value="" id="form2Example31" checked />
                        <label class="form-check-label" for="form2Example31"> Remember me </label>
                    </div>
                </div>

                <div class="col">
                    <!-- Simple link -->
                    <a href="#!">Forgot password?</a>
                </div>
            </div>

            <!-- Submit button -->
            <button @click="submitForm" type="submit" class="btn btn-outline-dark btn-block mb-4">Login</button>

            <!-- Register buttons -->
            <div class="text-center">
                <p>Not a member? <router-link to="/signup">Register</router-link></p>
                <p>or sign up with:</p>
                <button type="button" class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-facebook-f"></i>
                </button>

                <button type="button" class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-google"></i>
                </button>

                <button type="button" class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-twitter"></i>
                </button>

                <button type="button" class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-github"></i>
                </button>
            </div>
        </div>
    </form>
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

                    axios.defaults.headers.common['Authorization'] = "Token " + token

                    localStorage.setItem('token', token)

                    this.$router.push('/')
                })
                .catch(error => {
                    console.log(error);
                })
        }
    }
}
</script>
<style ></style>