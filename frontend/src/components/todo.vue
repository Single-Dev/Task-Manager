<template>
    <section class="gradient-custom">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col col-xl-10">

                    <div class="card">
                        <div class="card-body p-5">
                            <addTask :user_id="user_id" @CreateTask="$emit('CreateTask', $event)" />

                            <Filter :UpdateFilterHandler="UpdateFilterHandler" :filterName="filter" />
                            <div v-if="isLoading" class="d-flex justify-content-center p-5">
                                <loader />
                            </div>
                            <items v-else :tasks="onFilterHandler(tasks, filter)"
                                @checkToggle="$emit('checkToggle', $event)" @deleteTask="$emit('deleteTask', $event)" />
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>
</template>
<script>
import addTask from '@/components/todo/addTask.vue'
import Filter from '@/components/todo/filter.vue'
import items from '@/components/todo/items.vue'

export default {
    components: {
        addTask,
        Filter,
        items
    },
    data() {
        return {
            filter: 'active'
        }
    },
    props: {
        isLoading: {
            type: Boolean,
            required: true
        },
        user_id: {
            type: Number,
            required: true
        },
        tasks: {
            type: Array,
            required: true
        },
    },
    methods: {
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
    }
}
</script>
<style scoped>
.gradient-custom{
    width: 100%;
    height: auto;
    background-image: linear-gradient(-20deg, #ff2846 0%, #6944ff 100%);
    padding-bottom:360px ;
}

.card{
    box-shadow: 0px 8px 60px -10px rgba(13, 28, 39, 0.6);
}
</style>