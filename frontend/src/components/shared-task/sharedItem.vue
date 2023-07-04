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
                <span v-for="user in users">
                    <a :href="'/@' + user.username">
                        <img src="#"  alt="avatar"
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
            users:[],
        }
    },
    methods: {
        async getUsers(){
            const response = await axios.get('/api/users/')
            response.data.forEach(e => {
                this.sharredTask.users.forEach(r =>{
                    if (r == e.id) {
                        console.log(e.username);
                        this.users.push(e)
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