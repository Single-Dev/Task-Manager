<template>
    <div class="card" style="border-radius: 15px;">
        <div class="card-body p-4">
            <h3 class="mb-3">{{ sharredTask.name }}</h3>
            <p class="small mb-0"><i class="fas fa-star fa-lg text-warning"></i> <span class="mx-2">|</span>
                Public <span class="mx-2">|</span> Updated by <strong>MDBootstrap</strong> on 11 April ,
                2021
            </p>
            <hr class="my-4">
            <div class="d-flex justify-content-start align-items-center">
                <p class="mb-0 text-uppercase"><i class="fas fa-cog me-2"></i> <span
                        class="text-muted small">settings</span></p>
                <p class="mb-0 text-uppercase"><i class="fas fa-link ms-4 me-2"></i> <span class="text-muted small">program
                        link</span></p>
                <p class="mb-0 text-uppercase"><i class="fas fa-ellipsis-h ms-4 me-2"></i> <span
                        class="text-muted small">program link</span>
                    <span class="ms-3 me-4">|</span>
                </p>
                <span v-for="user in SharedTaskUsers">
                    <a :href="'/@' + user.username">
                        <img :src="'http://127.0.0.1:8000'+ user.profile_photo"  alt="avatar"
                        class="img-fluid rounded-circle me-1" width="35">
                        @{{ user.username }}
                    </a>
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
        sharredTask:{
            type: Array,
            required: true
        }
    },
    data() {
        return {
            SharedTaskUsers:[],
        }
    },
    methods: {
            async getUsers(){
                const response = await axios.get('/api/users/')
                const profiles = await axios.get('/api/profiles/')
                response.data.forEach(e => {
                    this.sharredTask.users.forEach(user_id =>{
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
            }
    },
    mounted() {
        this.getUsers()
    },
}
</script>
<style>
    
</style>