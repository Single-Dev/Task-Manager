<template>
    <!-- Tabs content -->
    <div class="tab-content" id="ex1-content">
        <div v-if="!tasks.length" class="p-3">
            <h2>Topilamdi</h2>
        </div>
        <div v-else class="tab-pane fade show active" id="ex1-tabs-1" role="tabpanel" aria-labelledby="ex1-tab-1">
            <ul v-for="task in tasks" class="list-group mb-0">
                <li class="list-group-item d-flex align-items-center border-0 mb-2 rounded mt-3 justify-content-between">
                    <div class="mx-4">
                        <input
                        @click="$emit('checkToggle', task)"
                        class="form-check-input my-2"
                        type="checkbox"
                        :checked="task.done"/>

                        <label @click="$emit('checkToggle', task)">
                        {{ task.name }}
                        </label>
                    </div>
                    <div>
                        <router-link class="fa-solid fa-pen text-dark" :to="'/task/' + task.id"></router-link>
                        <i @click="$emit('deleteTask', task)" class="mx-4 text-danger fa-solid fa-trash"></i>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        tasks: {
            type: Object,
            required: false
        },
        user_id: {
            type: Number,
            required: true
        }
    }
}
</script>
<style scoped>
    i{
        cursor: pointer !important;
    }
    li{
        background-color: #f4f6f7;
    }
</style>