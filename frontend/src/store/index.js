import { createStore } from 'vuex'

export default createStore({
  state: {
    token: '',
    IsAuthenticated: false
  },
  mutations: {
    initializeStore(state){
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.IsAuthenticated = true
      }else{
        state.token = ''
        state.IsAuthenticated = false
      }
    },
    setToken(state, token){
      state.token = token
      state.IsAuthenticated = true
    },
    removeToken(state){
      state.token = ''
      state.IsAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})
