<template>
    <div class="card mt-2">
        <div class="card-body p-4">
            <h3 class="mb-3">{{ sharedTask.name }}</h3>
            <p class="small mb-0"><i class="fas fa-star fa-lg text-warning"></i> <span class="mx-2">|</span>
                Public <span class="mx-2">|</span> Created by <strong><router-link :to="'/@' + sharedTaskOwner">@{{ sharedTaskOwner }}</router-link></strong> on {{ sharedTask.created_on }}
            </p>
            <hr class="my-4">
            <div class="d-flex justify-content-start align-items-center">
                <p class="mb-0 text-uppercase"><i class="fas fa-cog me-2"></i> <span
                        class="text-muted small">settings</span></p>
                <p class="mb-0 text-uppercase">
                    <span class="ms-2 me-2">|</span>
                    <router-link class="text-muted small" :to="'shared/' + sharedTask.id">Visit</router-link>
                    <span class="ms-2 me-2">|</span>
                </p>
                <span v-for="user in SharedTaskUsers">
                    <router-link :to="'/@' + user.username">
                        <img :src="apiBaseURL + user.profile_photo"  alt="avatar"
                        class="img-fluid rounded-circle me-1" width="35">
                    @{{ user.username }}
                    </router-link>
                </span>

                <button type="button" class="btn btn-outline-dark btn-sm btn-floating">
                    <i class="fas fa-plus"></i>
                </button>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    
    props:{
        sharedTask:{
            type: Array,
            required: true
        },
        apiBaseURL:{
            type: String,
            required: true
        }
    },
    data() {
        return {
            SharedTaskUsers:[],
            sharedTaskOwner: '',
            apiBaseURL: axios.defaults.baseURL
        }
    },
    methods: {
            async getUsers(){
                const response = await axios.get('/api/users/')
                const profiles = await axios.get('/api/profiles/')
                response.data.forEach(e => {
                    this.sharedTask.users.forEach(user_id =>{
                        if (user_id == e.id) {
                            const profile = profiles.data.find(profile => profile.user === e.id);
                            const newArr = {
                                id: e.id,
                                first_name: e.first_name,
                                username: e.username,
                                profile_photo: profile.profile_photo
                            }
                            this.SharedTaskUsers.push(newArr)
                    }
                    })
                });
            },
            async getSharedTaskOwnerInfo(){
                const response = await axios.get(`/api/user/id/${this.sharedTask.owner}/`)
                this.sharedTaskOwner = response.data.username
            }
    },
    mounted() {
        // this.getUsers()
        this.getSharedTaskOwnerInfo()
    },
}
</script>
<style>
    .card{
        border-radius: 15px !important;
    }
</style>