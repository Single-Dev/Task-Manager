<template>
    <div class="gradient-custom">
        <section class="d-flex justify-content-center align-items-center">
            <div class="row">
                <addSharedTasksVue :apiBaseURL="apiBaseURL" :user_id="user_id"/>
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
import addSharedTasksVue from '@/components/shared/addSharedTasks.vue'
export default {
    name: 'sharedTasks',
    components: {
        sharedItem,
        addSharedTasksVue
    },
    props: {
        apiBaseURL: {
            type: String,
            required: true
        },
        // users: {
        //     type: Array,
        //     required: true
        // },
        user_id: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            sharedTasks: [],
            isLoading: false,
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
        
    },
    mounted() {
        this.getSharedTasks()
    },
}
</script>
<style scoped>
/* .gradient-custom {
    width: 100%;
    height: auto !important;
    padding: 20px 0px;
    background-image: linear-gradient(-20deg, #ff2846 0%, #6944ff 100%);
    padding-bottom:430px;
} */

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

.active {
    opacity: 1 !important;
    z-index: 2;
}
</style>