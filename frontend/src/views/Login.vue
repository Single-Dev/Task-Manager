<template>
   <form @submit.prevent class="form w-50">
            <input type="text" v-model="username" placeholder="Username" class="form-control mb-3">
            <input type="password" v-model="password" placeholder="Password" class="form-control mb-3">
            <button type="button" class="btn btn-outline-dark w-100" @click="authenticate">login</button>
    </form>
</template>
  
<script>
import axios from "axios";

export default {
    data() {
        return {
            username: "",
            password: "",
            email: ""
        };
    },
    methods: {
        authenticate() {
            const payload = {
                username: this.username,
                password: this.password,
                email: this.email,
            };
            axios
                .post('http://127.0.0.1:8000/api/v1/jwt/create/', payload)
                .then((response) => {
                    localStorage.setItem('token', response.data.access)
                    this.$store.commit("updateToken", {newToken: response.data.access});
                    // get and set auth user
                    const base = {
                        baseURL: 'http://127.0.0.1:8000/api/v1/users/',
                        headers: {
                            // Set your Authorization to 'JWT', not Bearer!!!
                            Authorization: `JWT ${localStorage.getItem('token')}`,
                            "Content-Type": "application/json",
                        },
                        xhrFields: {
                            withCredentials: true,
                        },
                    };
                    // Even though the authentication returned a user object that can be
                    // decoded, we fetch it again. This way we aren't super dependant on
                    // JWT and can plug in something else.
                    const axiosInstance = axios.create(base);
                    axiosInstance({
                        url: "/me/",
                        method: "get",
                        params: {},
                    }).then((response) => {
                        this.$store.commit("setAuthUser", {
                            authUser: response.data,
                            isAuthenticated: true,
                        });
                        this.$router.push({ name: "Home" });
                    });
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
};
</script>

<!-- <template >
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
                    // this.$store.commit('../store/setAccess', access)

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
    
</style> -->