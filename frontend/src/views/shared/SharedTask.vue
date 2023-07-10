<template>
    <div>
        <h1>{{SharedTaskDetails.name}}</h1>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'sharedTask',
    data() {
        return {
            SharedTaskDetails: {}
        }
    },
    methods: {
        async getSharedTaskDetails() {
            const response = await axios.get(`/api/shared-tasks/${this.$route.params.pk}/`)
            this.SharedTaskDetails = response.data
        },
    },
    mounted() {
        this.getSharedTaskDetails()
    },
}
</script>
<style lang="">
    
</style>