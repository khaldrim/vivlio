new Vue({
  el: '#app',
  data () {
    return {
      generos: [],
      title:'Poemas de amor'
    }
  },
  mounted () {
    axios
      .get('http://192.168.99.100:8000/api/books/get-book',{
        params: {
          title: this.title
      }
    })
      .then(response => {console.log(response); this.generos = response.data })
    }

  })
//headers: { 'title': this.title }
