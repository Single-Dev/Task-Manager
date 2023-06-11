<template>
    <section class="vh-100 gradient-custom">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col col-xl-10">

                    <div class="card">
                        <div class="card-body p-5">
                            <addTask :user_id="user_id" @CreateTask="$emit('CreateTask', $event)"/>
                            <navUl />
                            <content  :tasks="tasks" :user_id="user_id"/>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>
</template>
<script>
import addTask from '@/components/todo/addTask.vue'
import navUl from '@/components/todo/nav.vue'
import content from '@/components/todo/content.vue'

export default {
    components: {
        addTask,
        navUl,
        content
    },
    props: {
        user_id: {
            type: Number,
            required: true
        },
        tasks: {
            type: Array,
            required: true
        }
    }
}
</script>
<style></style>