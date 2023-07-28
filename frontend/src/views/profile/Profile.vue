<template>
    <div v-if="isLoading">
        loading
        <loader/>
    </div>
    <div v-else>
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
            user_datails: [],
            isLoading: false
        }
    },
    props: {
        username: {
            type: String,
            required: false
        }
    },
    methods: {
        async getUser() {
            try {
                this.isLoading = true
                const users = await axios.get('/api/users/')
                this.profile_username = this.$route.params.username
                users.data.forEach(e => {
                    if (this.profile_username == e.username) {
                        this.user_found = true
                    }
                });
            } catch (error) {
                alert(error.message)
            }finally{
                this.isLoading = false
            }
        },
        async getUserDetails() {
            try {
                // this.isLoading = true
                const response = await axios.get(`/api/users/${this.$route.params.username}/`)
                this.user_datails = response.data
            } catch (error) {
                alert(error.message)
            }finally{
                // this.isLoading = false
            }
        }
    },

    mounted() {
        this.getUser()
        this.getUserDetails()
    }
}
</script>
<style lang="">
    
</style>