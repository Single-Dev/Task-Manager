<template >
    <!-- Section: Design Block -->
    <section class="text-center">
        <!-- Background image -->
        <div class="p-5 bg-image bg"></div>
        <!-- Background image -->

        <div class="card mx-4 mx-md-5 shadow-5-strong bg_2">
            <div class="card-body py-5 px-md-5">

                <div class="row d-flex justify-content-center">
                    <div class="col-lg-8">
                        <h2 class="fw-bold mb-5">Sign up now</h2>
                        <form @submit.prevent>
                            <!-- Email input -->
                            <div class="form-outline mb-4">
                                <input type="email" id="email" class="form-control" v-model="email"/>
                                <label class="form-label" for="email">Email address</label>
                            </div>
                            <div class="form-outline mb-4">
                                <input type="text" id="username" class="form-control" v-model="username"/>
                                <label class="form-label" for="username">Username</label>
                            </div>
                            <!-- Password input -->
                            <div class="form-outline mb-4">
                                <input type="password" id="password" class="form-control" v-model="password"/>
                                <label class="form-label" for="password">Password</label>
                            </div>

                            <!-- Submit button -->
                            <button
                            @click="$emit('Signup', email, username, password)"
                            type="submit"
                            class="btn btn-outline-dark btn-block mb-4"
                            >
                                Sign up
                            </button>

                            <!-- Register buttons -->
                            <div class="text-center">
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
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
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
}
</script>
<style scoped>
.bg{
    background-image: url('https://mdbootstrap.com/img/new/textures/full/171.jpg');
    height: 300px;
}
.bg_2{
    margin-top: -100px;
    background: hsla(0, 0%, 100%, 0.8);
    backdrop-filter: blur(30px);
}
</style>