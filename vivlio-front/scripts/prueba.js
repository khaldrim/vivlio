
//var data = JSON.stringify({"title":"Poemas de amor"});
//'http://192.168.99.100:8000/api/books/' trae // TODO:
//Declarar la variables que sera utilizada por varias instancias!!!!

new Vue({
  el: '#seeker',
  data () {
    return {
      search:'',
      results:[]
    }
  },
  methods: {
       searchBook: function () {
           var config = {
             headers: {
               'Content-Type': 'application/json'
             },
             params: {
                   title__wildcard: this.search
                 }
           }
           axios
           .get('http://192.168.99.100:8000/api/books/', config)
           .then(response => {this.results = response.data; console.log(this.results)})
   }
  },
   computed: {
              // un getter computado
              message: function () {
              // `this` apunta a la instancia de vm
                return this.results
              }
  }
})
