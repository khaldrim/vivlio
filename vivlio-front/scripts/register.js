new Vue({
    el: '#app',
    data () {
      return {
        theme: ['profile-genre', 'profile-genre', 'profile-genre', 'profile-genre', 'profile-genre', 'profile-genre', 'profile-genre'],
        isActive: [false, false, false, false, false, false, false],
        name: "",
        lastname: "",
        email: "",
        pwd: "",
        genres: []
      }
    },
    methods: {
        toggleClass: function (position) {
            console.log(position);
            if(!this.isActive[position]) {
                this.isActive[position] = !this.isActive[position];
                this.theme[position] = "profile-genre-selected";
            } else {
                this.theme[position] = "profile-genre";
                this.isActive[position] = !this.isActive[position];
            }
        },
        addGenre: function (name, position) {
            if(!this.genres.includes(name)) {
                this.genres.push(name);
            } else {
                let index = this.genres.indexOf(name);
                if (index !== -1) {
                    this.genres.splice(index, 1)
                }
            }

            this.toggleClass(position);
        },
        sendData: function () {

            let user = {
                "rut": "1111111",
                "first_name": this.name,
                "last_name": this.lastname,
                "email": this.email,
                "password": this.pwd,
                "list_of_tags": this.genres
            }

            console.log(user);
            axios.post('http://localhost:8000/api/users/create', user)
                .then(result => {
                    console.log(result);
                })
                .catch(error => {
                    console.log(error);
                })   
        }
        // register:   
    },
    mounted () {        
    //   axios
    //     .get('http://localhost:8000/api/library/list-library')
    //     .then(response => {
    //         this.info = response.data.genres
    //         console.log(response)
    //     }).catch(error => {console.log(error)})
    }
  })
  


