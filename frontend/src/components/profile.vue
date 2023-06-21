<template>
    <div>
        <h1>hello {{ users }}</h1>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'profile',
    data() {
        return {
            users: [],
            userDetail: []
        }
    },

    methods: {
        async getUsers(){
            const response = await axios.get('api/users/')
            this.users = response.data
        },
        getUser() {
            this.users.forEach(e => {
                if (e.username == this.$route.params.username) {
                    this.userDetail = e;
                }
                console.log(e);
            });
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