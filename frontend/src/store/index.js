import {createStore} from 'vue'

export default createStore({
    initializeStore(state){
        if (localStorage.getItem('access')){
            state.access = localStorage.getItem('access')
        } else{
            state.access = ''
        }
    },
    setAccess(state, access){
        state.access = access
    }
})