<template>
    <div>
        <section class="vh-100" style="background-color: #5f59f7;">
            <div class="container py-5 h-100">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div v-for="sharedTask in sharedTasks" class="col col-xl-10">
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
            sharedTasks:[]
        }
    },
    components:{
        sharedItem
    },
    methods: {
        async getSharedTasks(){
            try {
                const response = await axios.get('/api/shared-tasks/')
                const r = await axios.get('/api/shared-tasks/1/')
                console.log(r)
                this.sharedTasks = response.data
            } catch (error) {
                alert(error.message)
            }
        }
    },
    mounted() {
        this.getSharedTasks()
    },
}
</script>
<style lang="">
    
</style>