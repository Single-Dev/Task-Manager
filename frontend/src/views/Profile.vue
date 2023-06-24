<template>
    <div>
        <div v-if="username == profile_username">
            <button>Edit</button>
        </div>
        <div v-else>
            <button>Follow</button>
        </div>
        <h1>@{{ profile_username }}</h1>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'profile',
    data() {
        return {
            profile_username: '',
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
                if (this.$route.params.username == e.username) {
                    this.profile_username = this.$route.params.username
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