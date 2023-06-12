<template>
    <!-- Tabs content -->
    <div class="tab-content" id="ex1-content">
        <div class="tab-pane fade show active" id="ex1-tabs-1" role="tabpanel" aria-labelledby="ex1-tab-1">
            <ul  v-for="task in tasks" class="list-group mb-0">
                <li class="list-group-item d-flex align-items-center border-0 mb-2 rounded" style="background-color: #f4f6f7;">
                    <input
                    class="form-check-input me-2"
                    type="checkbox" 
                    :checked="task.done"
                    @click="$emit('checkToggle', task)"
                    />
                    {{ task.name }}
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
export default {
props:{
    tasks:{
        type: Object,
        required: false
    },
    user_id:{
        type: Number,
        required: true
    }
}
}
</script>
<style lang="">
    
</style>