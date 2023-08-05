<template>
    <div v-if="getting_users">
        <loader/>
        loading
    </div>
    <div v-else class="gradient-custom">
        <div class="container py-5 h-100">
            <div class="d-flex justify-content-center align-items-center h-100">
                <div class="card">
                    <div class="card-body p-5">
                        {{ users }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Results',
    props: {
        getting_users: {
            type: Boolean,
            required: true
        },
        users: {
            type: Array,
            required: true,
        }
    }
}
</script>
<style scoped>
.gradient-custom {
    width: 100%;
    height: 100vh;
    background-image: linear-gradient(-20deg, #ff2846 0%, #6944ff 100%);
}

.card {
    width:800px;
    box-shadow: 0px 8px 60px -10px rgba(13, 28, 39, 0.6);
}
</style>