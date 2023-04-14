import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)
 
const store = new Vuex.Store({
    state:{
        access: "",
        refresh:""
    },
    mutations:{
        initializeStore(state){
            if (localStorage.getItem('access')){
                state.access = localStorage.getItem('access')
            } else{
                state.access = ''
            }
        },
        // setAccess(state){
        //     state.access = 
        // },
    },
    actions:{},
    modules:{}
})