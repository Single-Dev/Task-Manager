<template>
    <div>
        <section class="vh-100 gradient-custom">
            <div class="container py-5 h-100 main">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div v-if="!sharedTasks.length && !isLoading">
                        <h1>Topilmadi...</h1>
                    </div>
                    <div class="d-flex justify-content-center" v-else-if="isLoading">
                        <loader />
                    </div>
                    <div v-else v-for="sharedTask in sharedTasks" class="col col-xl-10">
                        <sharedItem :sharedTask="sharedTask" :apiBaseURL="apiBaseURL" />
                    </div>
                    <button @click="editProfileBtn" class="btn btn-outline-dark w-50">Add <i class="fas fa-add"></i></button>
                  
                    <div class="div p-5">
                        <form class="card-form p-2">
                            <div class="form__container p-2">
                                <input type="text" class="form-control" placeholder="Shared Task Name">
                                <input type="text" class="form-control mb-2 mt-2" placeholder="">
                                <input type="text" class="form-control" placeholder="">
                            </div>
                        </form>
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
    props: {
        apiBaseURL: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            sharedTasks: [],
            isLoading: false,
            owner: '',
            name:'',
            tasks:'',
            users:'',
            created_on: ''
        }
    },
    components: {
        sharedItem
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
        editProfileBtn() {
			let card = document.querySelector('.div')
			card.classList.toggle('active')
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
    height: auto;
    background-image: linear-gradient(-20deg, #ff2846 0%, #6944ff 100%);
}

.main{
    position: relative;
}
.div{
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    opacity: -1;
    transition: 500ms;
    transition-delay: 50ms;
}

.card-form{
    width: 580px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0px 8px 60px -10px rgba(13, 28, 39, 0.6);
}

.active{
    opacity: 1;
}

</style>