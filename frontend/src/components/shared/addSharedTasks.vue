<template>
    <div class="div">
        <button @click="btnToggle" class="btn btn-outline-dark">Add</button>
    </div>
    <div class="box">
        <div class="card-form">
            <form @submit.prevent>
                <input type="text" class="form-control" v-model="name" placeholder="Shared Task Name">
                <input type="text" class="form-control mt-2 mb-2" placeholder="Tasks" @input="UpdateTasksTerm"
                    v-model="tasks_term">
                <div class="card" v-if="searched_tasks.length > 0">
                    <ul class="list-group mb-0">
                        <div v-if="!searched_tasks.length && !isTasksLoading">
                            <h6 v-if="tasks_term.length > 0">Topilmadi...</h6>
                        </div>
                        <div v-else-if="isTasksLoading" class="d-flex justify-content-center align-items-center p-2">
                            <loader />
                        </div>
                        <div v-else>
                            <div class="d-flex flex-wrap">
                                <div v-for="task in toAddTasks">
                                    <div class="border m-2 rounded p-2">
                                        Id:{{ task }}
                                        <i class="fas fa-close text-danger"></i>
                                    </div>
                                </div>
                            </div>
                            <li v-for="task in searched_tasks"
                                class="list-group-item d-flex align-items-center border-0 mb-2 rounded mt-3 justify-content-between">
                                    <h6>{{ task.name }}</h6>
                                    <div class="d-flex align-items-center">
                                        <h6 class="mx-2">status: {{ task.done }}</h6>
                                        <input type="checkbox" v-model="task.selected">
                                    </div>
                            </li>
                            <button class="w-100 btn btn-outline-info my-2"  @click="toAddTasksFunc">Add</button>
                        </div>
                    </ul>
                </div>
                <input type="text" class="form-control" placeholder="Username" @input="UpdateUsersTerm"
                    v-model="users_term">

                <div class="card" v-if="searched_users.length > 0">
                    <ul class="list-group mb-0">
                        <div v-if="!searched_users.length && !isUsersLoading">
                            <h6 v-if="users_term.length > 0">Topilmadi...</h6>
                        </div>
                        <div v-else-if="isUsersLoading" class="d-flex justify-content-center align-items-center p-2">
                            <loader />
                        </div>
                        <div v-else>
                            <div class="d-flex flex-wrap">
                                <div v-for="user in toAddUsers">
                                    <div class="border m-2 rounded p-2">
                                        Id:{{ user }}
                                        <i class="fas fa-close text-danger"></i>
                                    </div>
                                </div>
                            </div>
                            <li v-for="user in searched_users"
                                class="list-group-item d-flex align-items-center border-0 mb-2 rounded mt-3 justify-content-between">
                                <div class="mx-2 d-flex align-items-center">
                                    <img :src="apiBaseURL + user.profile_photo" alt="avatar"
                                        class="img-fluid rounded-circle me-1 ml-2" width="35">
                                    <h6 class="m-0">{{ user.first_name }}</h6>
                                </div>
                                <div>
                                    <router-link class="text-dark mx-2" :to="'/@' + user.username">@{{ user.username }}</router-link>
                                    <input type="checkbox" v-model="user.selected">
                                </div>
                            </li>
                        </div>
                        <button class="btn btn-outline-info" @click="toAddUsersFunc">Add</button>
                    </ul>
                </div>
                <div class="d-flex mt-2">
                    <button class="btn btn-dark w-50 mr-2" @click="submitForm">Add</button>
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
            isTasksLoading: false,
            isUsersLoading: false,
            toAddTasks: [],
            toAddUsers: []
        }
    },
    props: {
        apiBaseURL: {
            type: String,
            required: true
        },
        user_id:{
            type: Number,
            required: true
        }
    },
    methods: {
        async submitForm(){
            const formData = {
                owner: this.user_id,
                name: this.name,
                tasks: this.toAddTasks,
                users: this.toAddUsers,
                created_on: new Date()
            }
            try {
                const response =  await axios.post('/api/add-shared-task/', formData)
                console.log(response);
            } catch (error) {
                alert(error.message)
            } finally{
                this.$router.push('/shared-tasks')
            }
        },
        btnToggle() {
            let card = document.querySelector('.card-form')
            card.classList.toggle('active')
        },
        async SearchForUser(term) {
            try {
                this.searched_users = [];
                this.isUsersLoading = true
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
            } finally{
                this.isUsersLoading = false
            }
        },
        async SearchForTasks(term) {
            try {
                this.isTasksLoading = true
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
            } catch (error) {
                console.log(error.message);
            } finally {
                this.isTasksLoading = false
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
        toAddTasksFunc() {
            this.toAddTasks = []
            this.searched_tasks.forEach(e=>{
                if(e.selected == true){
                    this.toAddTasks.push(e.id)
                }
            })
            this.tasks_term = ''
        },
        toAddUsersFunc(){
            this.toAddUsers = []
            this.searched_users.forEach(e=>{
                if(e.selected == true){
                    this.toAddUsers.push(e.id)
                    console.log(this.toAddUsers);
                }
            })
            console.log(this.toAddUsers);
        },
    },
}
</script>
<style scoped>
body{
    transition: 5s;
}

.div{
    margin-top: 50px;
}

.card li {
    background-color: #f4f6f7;
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;
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

.active {
    opacity: 1 !important;
    z-index: 2;
}

</style>