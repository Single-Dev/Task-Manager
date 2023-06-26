<template>
    <div>
        <div v-if="username == profile_username">
            <button>Edit</button>
        </div>
        <div v-else>
            <button>Follow</button>
        </div>
        <h1 v-if="user_found">@{{ profile_username }}</h1>
        <h1 v-else>Siz buni band qiling: @{{ profile_username }}</h1>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'profile',
    data() {
        return {
            profile_username: '',
            user_found: false,
        }
    },
    props:{
        username:{
            type:String,
            required: false
        }
    },
    methods: {
        async getUser() {
            const users = await axios.get('/api/users/')
            users.data.forEach(e => {
                this.profile_username = this.$route.params.username
                if (this.$route.params.username == e.username) {
                    this.user_found = true
                }else{
                    this.user_found = false
                }
            });
        }
    },

    mounted() {
        this.getUser()
    }
}
</script>
<style lang="">
    
</style>