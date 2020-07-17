new Vue({
  el: '#app',
  data () {
    return {
      info: null
    }
  },
  mounted () {
    axios
      .get('http://192.168.99.102:8000/api/genres/list-all')
      .then(response => (this.info = response.data.genres))
      }
})

