import { createStore } from "vuex" 

const store = createStore({
    state: {
        isLoggedin: false,
        array: [],
        favarr: [],
        render: false,
    },
    mutations: {
        login: state => state.isLoggedin = true,
        logout: state => state.isLoggedin = false,
        arraydata(state, arraydata){
            state.array = arraydata 
        },
        favarr(state,arraydata){
            state.favarr = arraydata
        },
        setrenderT: state => state.render = true,
        setrenderF: state => state.render = false,
    },
})
export default store