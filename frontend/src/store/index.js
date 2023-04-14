import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";


// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default new Vuex.Store({
  state: {
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem("token"),
    // endpoints: {
    //   // TODO: Remove hardcoding of dev endpoints
    //   obtainJWT: "http://127.0.0.1:8000/api/v1/jwt/create/",
    //   refreshJWT: "http://127.0.0.1:8000/api/v1/jwt/refresh_token/",
    //   baseUrl: "http://127.0.0.1:8000/",
    // },
  },

  mutations: {
    setAuthUser(state, { authUser, isAuthenticated }) {
      Vue.set(state, "authUser", authUser);
      Vue.set(state, "isAuthenticated", isAuthenticated);
    },
    updateToken(state, newToken) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.setItem("token", newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.removeItem("token");
      state.jwt = null;
    },
  },
});

// // import Vuex from 'vuex'
// // import Vue from 'vue'
// import { createStore } from 'vuex'

// // Vue.use(Vuex)
 
// export default createStore({
//     state:{
//         access: "",
//         refresh:""
//     },
//     mutations:{
//         initializeStore(state){
//             if (localStorage.getItem('access')){
//                 state.access = localStorage.getItem('access')
//             } else{
//                 state.access = ''
//             }
//         },
//         setAccess(state){
//             state.access = localStorage.getItem('access')
//         }
//     },
//     actions:{},
//     modules:{}
// })