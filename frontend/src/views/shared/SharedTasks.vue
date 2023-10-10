<template>
    <div class="gradient-custom">
        <section class="d-flex justify-content-center align-items-center">
            <div class="row">
                <div class="ps-r">
                    <div class="div">
                        <button @click="btnToggle" class="btn btn-outline-dark">Add</button>
                    </div>
                    <div class="card-form">
                        <form @submit.prevent>
                            <input type="text" class="form-control" v-model="name" placeholder="Shared Task Name">
                            <input type="number" class="form-control mt-2 mb-2" placeholder="Task id. e.g. 1">
                            <input type="text" class="form-control" placeholder="e.g. username, username_1">
                            
                            <div class="d-flex mt-2">
                                <button class="btn btn-dark w-50 mr-2" @click="addSharedTask">Add</button>
                                <button class="btn btn-outline-danger w-50" @click="btnToggle">Cancel</button>
                            </div>
                        </form>
                    </div>
                </div>
                <div v-if="!sharedTasks.length && !isLoading">
                    <h2>Topilmadi..</h2>
                </div>
                <div v-else-if="isLoading">
                    <loader />
                </div>
                <div v-else>
                    <div v-for="sharedTask in sharedTasks">
                        <sharedItem :sharedTask="sharedTask" />
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>
<script>
import axios from 'axios'
import sharedItem from '@/components/shared/sharedItem.vue'
export default {
    name: 'sharedTasks',
    components: {
        sharedItem
    },
    props: {
        apiBaseURL: {
            type: String,
            required: true
        },
        users: {
            type: Array,
            required: true
        },
        user_id: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            sharedTasks: [],
            isLoading: false,
            owner: '',
            name: '',
            tasks: '',
            users: [],
            created_on: ''
        }
    },
    methods: {
        async getSharedTasks() {
            try {
                this.isLoading = true
                const response = await axios.get('/api/shared-tasks/')
                this.sharedTasks = response.data
            } catch (error) {
                alert(error.message)
            } finally {
                this.isLoading = false
            }
        },
        async addSharedTask() {
            try {
                const userInfo = await axios.get(`/api/users/bekzodbek/`)
                this.users.push(userInfo.data.id)
                console.log(this.users);
            } catch (error) {
                console.log(error.message);
            }
            const formData = {
                owner: this.user_id,
                name: this.name,
                tasks: [this.tasks],
                users: [this.users],
                created_on: new Date()
            }

            try {
                const response = await axios.post('/api/add-shared-task/', formData)
                this.sharedTasks.push(response.data)
                this.isLoading = true
            } catch (error) {
                alert(error.message)
            } finally {
                this.isLoading = false
                this.name = ''
                this.tasks = ''
                this.users = ''
            }
            this.btnToggle()
        },
        btnToggle() {
            let card = document.querySelector('.card-form')
            card.classList.toggle('active')
            console.log(this.users);
        },
    },
    mounted() {
        this.getSharedTasks()
    },
}
</script>
<style scoped>
.gradient-custom {
    width: 100%;
    height: auto !important;
    padding: 20px 0px;
    background-image: linear-gradient(-20deg, #ff2846 0%, #6944ff 100%);
    padding-bottom:430px;
}

.ps-r {
    position: relative;
    width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.div{
    padding: 20px 0px;
}

.card-form {
    width: 580px;
    padding: 10px;
    position: absolute;
    top: 20px;
    opacity: 0;
    z-index: -1;
    transition: 500ms;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0px 8px 60px -10px rgba(13, 28, 39, 0.6);
}

/* .card-form{
} */

.active {
    opacity: 1 !important;
    z-index: 2;
}
</style>