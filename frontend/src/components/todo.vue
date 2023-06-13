<template>
    <section class="vh-100 gradient-custom">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col col-xl-10">

                    <div class="card">
                        <div class="card-body p-5">
                            <addTask
                            :user_id="user_id"
                            @CreateTask="$emit('CreateTask', $event)" />

                            <Filter
                            :UpdateFilterHandler="UpdateFilterHandler"
                            :filterName="filter"
                            />


                            <content
                            :tasks="onFilterHandler(tasks, filter)"
                            :user_id="user_id"
                            @checkToggle="$emit('checkToggle', $event)"
                            @deleteTask="$emit('deleteTask', $event)"
                            />
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
import content from '@/components/todo/content.vue'

export default {
    components: {
        addTask,
        Filter,
        content
    },
    data() {
        return {
            filter: 'all'
        }
    },
    props: {
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
                    return arr.filter(c => c.done == false)
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
<style></style>