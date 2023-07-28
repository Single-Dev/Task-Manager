<template>
    <div>
        <section class="vh-100" style="background-color: #5f59f7;">
            <div class="container py-5 h-100">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div v-if="isFound == false">
                        <h1>Topilmadi...</h1>
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
            isFound: false,
            isLoading: false
        }
    },
    components:{
        sharedItem
    },
    methods: {
        async getSharedTasks(){
            try {
                const response = await axios.get('/api/shared-tasks/')
                this.sharedTasks = response.data
                if(this.sharedTasks.length > 0){
                this.isFound = true
                }else{
                    this.isFound = false
                }
                this.isLoading = true
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