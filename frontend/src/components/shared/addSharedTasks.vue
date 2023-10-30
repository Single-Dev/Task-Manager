<template>
    <div class="ps-r">
        <div class="div">
            <button @click="btnToggle" class="btn btn-outline-dark">Add</button>
        </div>
        <div class="card-form">
            <form @submit.prevent>
                <input type="text" class="form-control" v-model="name" placeholder="Shared Task Name">
                <input type="number" class="form-control mt-2 mb-2" placeholder="Task id. e.g. 1">
                <input
                type="text"
                class="form-control"
                placeholder="e.g. username, username_1"
                @input="UpdateTerm"
                v-model="term"
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
            term: ''
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
        async test(term) {
            const r = await axios.get(`/api/users/?search=${this.term}`)
            console.log(r);
        },
        UpdateTerm(e) {
            this.term= e.target.value
            this.test(this.term)
        },
    },
}
</script>
<style lang="">
    
</style>