import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import signUp from '@/store/signUp.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    query: '',
    books: []
  },
  mutations: {
    books (state, data) {
      state.books = data;
    },
    query (state, data) {
      state.query = data;
    }
  },
  actions: {
    setQuery: async function({commit, _ }, q) {
      commit('query', q);
    },
    getBook: async function ({ commit, state }, title) {
      const params = '*' + title + '*'
      let data = []
      
      await axios.get(`http://0.0.0.0:8000/api/books/?title__wildcard=${params}`)
        .then(response => (data = response.data))
        .catch(error => { console.log(error) });
      
        console.log(data);

      commit('books', data);
    },
    searchQuery: async function({commit, state}, query) {
      const params = '*' + query + '*'
      let data = []
      
      await axios.get(`http://0.0.0.0:8000/api/books/?title__wildcard=${params}`)
        .then(response => (data = response.data))
        .catch(error => { console.log(error) });
      
        console.log(data);

      commit('books', data);
      commit('query', query);
      
    }
  },
  modules: {
    signUp
  }
})
