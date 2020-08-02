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
<<<<<<< HEAD
    })
      .then(response => {console.log(response); this.generos = response.data })
    }

  })
//headers: { 'title': this.title }
=======
})

>>>>>>> 5696e9d34e20abd4909e94a4e845b230c07cd918
