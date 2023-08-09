<template>
    <section class="vh-100 gradient-custom">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col col-xl-10">

                    <div class="card">
                        <div class="card-body p-5">
                            <div>
                                <h1>{{ SharedTaskDetails.name }}</h1>
                                <p>Craeted by <router-link :to="'/@' + SharedTaskDetails.owner">{{ SharedTaskDetails.owner
                                }}</router-link> Craeted on: {{ SharedTaskDetails.created_on }}</p>
                            </div>
                            <addSharedTask />

                            <Filter :UpdateFilterHandler="UpdateFilterHandler" :filterName="filter" />
                            <div v-if="isLoading" class="d-flex justify-content-center p-5">
                                <loader />
                            </div>
                            <shareditems v-else :tasks="tasks" />
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>
</template>
<script>
import axios from 'axios';
import addSharedTask from '@/components/shared/addSharedTask.vue'
import Filter from '@/components/todo/filter.vue'
import shareditems from '@/components/todo/items.vue'
export default {
    name: 'sharedTask',
    components: {
        addSharedTask,
        Filter,
        shareditems
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
            } catch (error) {
                console.log(error);
            } finally {
                this.isLoading = false
            }
        },
        // getSharedTasks() {
        //     this.tasks = []
        //     // let arr = JSON.parse(JSON.stringify(this.SharedTaskDetails))
        //     let p =this.SharedTaskDetails.isArray
        //     // Object.prototype.toString.call(p) // [object Array]
        //     // Array.isArray(p) 


        // },
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
    },
    mounted() {
        this.getSharedTaskDetails()
        // this.getSharedTasks()
    },
}
</script>
<style lang="">
    
</style>