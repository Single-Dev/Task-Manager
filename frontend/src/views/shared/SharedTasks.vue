<template>
    <div>
        <section class="vh-100" style="background-color: #5f59f7;">
            <div class="container py-5 h-100">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div v-if="!sharedTasks.length  && !isLoading">
                        <h1>Topilmadi...</h1>
                    </div>
                    <div class="d-flex justify-content-center" v-else-if="isLoading">
                        <loader/>
                    </div>
                    <div v-else v-for="sharedTask in sharedTasks" class="col col-xl-10">
                      <sharedItem 
                      :sharedTask="sharedTask"
                      />
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
    data() {
        return {
            sharedTasks:[],
            isLoading: false
        }
    },
    components:{
        sharedItem
    },
    methods: {
        async getSharedTasks(){
            try {
                this.isLoading = true
                const response = await axios.get('/api/shared-tasks/')
                this.sharedTasks = response.data
            } catch (error) {
                alert(error.message)
            }finally{
                this.isLoading = false
            }
        },
       
    },
    mounted() {
        this.getSharedTasks()
    },
}
</script>
<style lang="">
    
</style>