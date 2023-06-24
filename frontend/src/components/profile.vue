<template>
    <div>
        <h1>hello {{ users }}</h1>
    </div>
</template>
<script>
import axios from 'axios';
import {useRoute} from 'vue-router'

export default {
    name: 'profile',
    data() {
        return {
            users: [],
            userDetail: [],
            username: ''
        }
    },

    methods: {
        async getUsers(){
            const response = await axios.get('api/users/')
            this.users = response.data
        },
        getUser() {
            // this.users.forEach(e => {
            //     if (e.username == this.$route.params.username) {
            //         this.userDetail = e;
            //     }
            //     console.log(e);
            // });
            const route=useRoute()
            this.username = route.params
        }
    },

    mounted() {
        this.getUsers();
        this.getUser()
    }
}
</script>
<style lang="">
    
</style>