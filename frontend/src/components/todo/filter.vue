<template>
    <div class="btn-group">
        <button v-for="btn in FilterBtns" type="button"
        :class="[filterName == btn.name ? 'btn btn-dark' : 'btn btn-outline-dark']"
            @click="FilterFunc(btn.name)">
            {{ btn.title }}
        </button>
    </div>
</template>
<script>
export default {
    props:{
        UpdateFilterHandler:{
            type: Function,
            required: true
        },
        filterName:{
            type: String,
            required: true
        }
    },
    data(){
        return{
            filter: "",
            FilterBtns:[
            {
                title: 'All',
                name:'all'
            },
            {
                title: 'Active',
                name:'active'
            },
            {
                title: "Completed",
                name:'completed'
            },
            {
                title: "Schudle",
                name:'schudle'
            }
            ]
        }
    },
    methods: {
        FilterFunc(filter){
            this.filter = filter
            this.UpdateFilterHandler(this.filter)
        }
    },
}
</script>
<style lang="">
    
</style>