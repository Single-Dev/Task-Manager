<template>
    <section class="vh-100 gradient-custom">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col col-xl-10">

                    <div class="card">
                        <div class="card-body p-5">
                            <div>
                                <h1>{{ SharedTaskDetails.name }}</h1>
                            </div>
                            <addSharedTask :user_id="user_id"  @CreateTask="CreateTask"/>

                            <Filter :UpdateFilterHandler="UpdateFilterHandler" :filterName="filter" />
                            <div v-if="isLoading" class="d-flex justify-content-center p-5">
                                <loader />
                            </div>
                            <shareditems v-else
                            :tasks="onFilterHandler(tasks, filter)"
                            @checkToggle="$emit('checkToggle', $event)"
                            @deleteTask="deleteTask"
                            />
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>
</template>
<script>
import axios from 'axios';
import addSharedTask from '@/components/todo/addTask.vue'
import Filter from '@/components/todo/filter.vue'
import shareditems from '@/components/todo/items.vue'
export default {
    name: 'sharedTask',
    components: {
        addSharedTask,
        Filter,
        shareditems
    },
    props:{
        user_id: {
            type: Number,
            required: true
        },
    },
    data() {
        return {
            SharedTaskDetails: {},
            tasks: [],
            isLoading: false,
            filter: 'active'
        }
    },
    methods: {
        async getSharedTaskDetails() {
            try {
                this.isLoading = true
                const response = await axios.get(`/api/shared-tasks/${this.$route.params.pk}/`)
                this.SharedTaskDetails = response.data
                const nestedTasks = this.SharedTaskDetails.tasks; // Assuming this is an array of arrays
                const flattenedTasks = [].concat(...nestedTasks);
                for (const taskId of flattenedTasks) {
                    const response = await axios.get(`/api/tasks/${taskId}/`);
                    this.tasks.push(response.data)
                }
            } catch (error) {
                console.log(error);
            } finally {
                this.isLoading = false
            }
        },
        onFilterHandler(arr, filter) {
            switch (filter) {
                case 'completed':
                    return arr.filter(c => c.done == true)
                case 'active':
                    return arr.filter(c => c.done == false && c.reminder == null)
                default:
                    return arr
            }
        },
        UpdateFilterHandler(filter) {
            this.filter = filter
        },
        async CreateTask(item) {
            try {
                const taskInfo = await axios.post('/api/create-task/', item)
                this.tasks.unshift(taskInfo.data)
                this.SharedTaskDetails.tasks.unshift(taskInfo.data.id)
                await axios.post(`/api/updata/shared-todo/${this.$route.params.pk}/`, this.SharedTaskDetails)
            } catch (error) {
                alert(error.message)
            }
        },
        async deleteTask(item) {
            try {
                await axios.delete(`/api/delete/${item.id}/`, item)
                this.tasks = this.tasks.filter(c => c.id != item.id)
            } catch (error) {
                alert(error.message)
            }
        }
    },
    mounted() {
        this.getSharedTaskDetails()
    },
}
</script>
<style scoped>
.gradient-custom {
    width: 100%;
    height: auto !important;
    padding: 20px 0px;
    background-image: linear-gradient(-20deg, #ff2846 0%, #6944ff 100%);
    padding-bottom:360px;
}
</style>