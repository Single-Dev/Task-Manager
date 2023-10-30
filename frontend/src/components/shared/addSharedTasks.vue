<template>
    <div class="ps-r">
        <div class="div">
            <button @click="btnToggle" class="btn btn-outline-dark">Add</button>
        </div>
        <div class="card-form">
            <form @submit.prevent>
                <input type="text" class="form-control" v-model="name" placeholder="Shared Task Name">
                <input
                type="text"
                class="form-control mt-2 mb-2"
                placeholder="Tasks"
                @input="UpdateTasksTerm"
                v-model="tasks_term"
                >
                <input
                type="text"
                class="form-control"
                placeholder="e.g. username, username_1"
                @input="UpdateUsersTerm"
                v-model="users_term"
                >

                <div class="d-flex mt-2">
                    <button class="btn btn-dark w-50 mr-2" @click="addSharedTask">Add</button>
                    <button class="btn btn-outline-danger w-50" @click="btnToggle">Cancel</button>
                </div>
            </form>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            users:[],
            name: '',
            users_term: '',
            tasks_term: ''
        }
    },
    methods: {
        async addSharedTask() {
            // try {
            //     const userInfo = await axios.get(`/api/users/bekzodbek/`)
            //     this.users.push(userInfo.data.id)
            //     console.log(this.users);
            // } catch (error) {
            //     console.log(error.message);
            // }
            const formData = {
                owner: this.user_id,
                name: this.name,
                // tasks: [this.tasks],
                // users: [this.users],
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
                // this.name = ''
                // this.tasks = ''
                // this.users = ''
            }
            this.btnToggle()
        },
        btnToggle() {
            let card = document.querySelector('.card-form')
            card.classList.toggle('active')
            console.log(this.users);
        },
        async SearchForUser(term) {
            try {
                const response = await axios.get(`/api/users/?search=${term}`)
                console.log(response.data);
            } catch (error) {
                console.log(error.message);
            }
        },
        async SearchForTasks(term) {
            try {
                const response = await axios.get(`/api/tasks-list/?search=${term}`)
                console.log(response.data);
            } catch (error) {
                console.log(error.message);
            }
        },
        UpdateUsersTerm(e) {
            this.users_term= e.target.value
            this.SearchForUser(this.users_term)
        },
        UpdateTasksTerm(e) {
            this.tasks_term= e.target.value
            this.SearchForTasks(this.tasks_term)
        },
    },
}
</script>
<style lang="">
    
</style>