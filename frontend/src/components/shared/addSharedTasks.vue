<template>
    <div class="ps-r">
        <div class="div">
            <button @click="btnToggle" class="btn btn-outline-dark">Add</button>
        </div>
        <div class="card-form">
            <form @submit.prevent>
                <input type="text" class="form-control" v-model="name" placeholder="Shared Task Name">
                <input type="text" class="form-control mt-2 mb-2" placeholder="Tasks" @input="UpdateTasksTerm"
                    v-model="tasks_term">
                <div class="card" v-if="searched_tasks.length > 0">
                    <div class="p-1" v-for="searched_task in searched_tasks">
                        <div class="d-flex justify-content-around align-items-center">
                            <input type="checkbox" v-model="searched_task.selected">
                            <p class="paragaph">{{ searched_task.name }}</p>
                            <p class="paragaph">status: {{ searched_task.done }}</p>
                        </div>
                    </div>
                </div>
                <input type="text" class="form-control" placeholder="e.g. username, username_1" @input="UpdateUsersTerm"
                    v-model="users_term">
                <div class="card" v-if="searched_users.length > 0">
                    <div class="p-1" v-for="searched_user in searched_users">
                        <input type="checkbox" v-model="searched_user.selected">
                        <img :src="apiBaseURL + searched_user.profile_photo" alt="avatar" class="img-fluid rounded-circle me-1" width="35">
                        <p>{{ searched_user.first_name }}</p>
                        <a :href="'/@'+ searched_user.username">@{{ searched_user.username }}</a>
                    </div>
                </div>
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
            users: [],
            name: '',
            users_term: '',
            tasks_term: '',
            searched_tasks: [],
            searched_users: [],
        }
    },
    props:{
        apiBaseURL:{
            type:String,
            required: true
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
                this.searched_users = [];
                const response = await axios.get(`/api/users/?search=${term}`)
                const profiles = await axios.get('/api/profiles/')
                response.data.forEach(e => {
                    const profile = profiles.data.find(profile => profile.user === e.id);
                    const user = {
                        id: e.id,
                        first_name: e.first_name,
                        username: e.username,
                        profile_photo: profile.profile_photo,
                        selected: false
                    }
                    this.searched_users.push(user)
                    console.log(user)
                })
            } catch (error) {
                console.log(error.message);
            }
        },
        async SearchForTasks(term) {
            try {
                this.searched_tasks = []
                const response = await axios.get(`/api/search-task/?search=${term}`)
                response.data.forEach(e => {
                    const tasks = {
                        id: e.id,
                        name: e.name,
                        done: e.done,
                        owner: e.owner,
                        selected: false,
                    }
                    this.searched_tasks.push(tasks)
                })
                console.log(response.data);
            } catch (error) {
                console.log(error.message);
            } finally {
            }
        },
        UpdateTasksTerm(e) {
            this.tasks_term = e.target.value
            if (this.tasks_term.length > 3) {
                this.SearchForTasks(this.tasks_term)
            }
        },
        UpdateUsersTerm(e) {
            this.users_term = e.target.value
            if (this.users_term.length > 3) {
                this.SearchForUser(this.users_term)
            }
        },
    },
}
</script>
<style scoped>
    .paragaph{
        margin-top: 15px;
    }
</style>