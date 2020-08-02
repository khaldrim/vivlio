import axios from 'axios'

export default ({
  namespaced: true,
  state: {
    genres: []
  },
  mutations: {
    genres (state, data) {
      state.genres = data
    }
  },
  actions: {
    getGenres: async function ({ commit }) {
      let data = []
      await axios.get('http://192.168.99.100:8000/api/tags/list-tags')
        .then(response => (data = response.data))
      commit('genres', data)
    }
  }
})
