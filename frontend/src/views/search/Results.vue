<template>
    <div class="gradient-custom">
        <div class="container py-5 h-100">
            <div class="d-flex justify-content-center align-items-center h-100">
                <div class="card">
                    <div class="card-body p-5">
                        <div v-if="!users.length && !getting_users">
                            <h4>Topilmadi...</h4>
                        </div>
                        <div class="d-flex justify-content-center align-items-center" v-else-if="getting_users">
                            <loader />
                        </div>
                        <div v-else>
                            <ul class="list-group mb-0">
                                <li v-for="user in users" class="list-group-item d-flex align-items-center border-0 mb-2 rounded mt-3 justify-content-between">
                                    <div class="mx-4">
                                        <img
                                        :src="apiBaseURL + user.profile_photo"
                                        alt="avatar"
                                        class="img-fluid rounded-circle me-1"
                                        width="35">
                                    </div>
                                    <div>
                                        <h6 class="m-0">{{ user.first_name }}</h6>
                                    </div>
                                    <div>
                                        <router-link class="text-dark" :to="'/@'+ user.username ">@{{ user.username }}</router-link>
                                    </div>
                                </li>
                            </ul>
                        </div>
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
        },
        apiBaseURL:{
            type: String,
            required: true
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
    width: 800px;
    box-shadow: 0px 8px 60px -10px rgba(13, 28, 39, 0.6);
}
.card li{
    background-color: #f4f6f7;
}
</style>