<template>
    <div>
        <section class="vh-100" style="background-color: #5f59f7;">
            <div class="container py-5 h-100">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div v-for="sharredTask in sharredTasks" class="col col-xl-10">
                      <sharedItem 
                      :sharredTask="sharredTask"
                      />
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>
<script>
import axios from 'axios'
import sharedItem from '@/components/shared-task/sharedItem.vue'
export default {
    name: 'SharedTasks',
    data() {
        return {
            sharredTasks:[]
        }
    },
    components:{
        sharedItem
    },
    methods: {
        async getSharedTasks(){
            try {
                const response = await axios.get('/api/shared-task/')
                this.sharredTasks = response.data
                console.log(this.sharredTasks);
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