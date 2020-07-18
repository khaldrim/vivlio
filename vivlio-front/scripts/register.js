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
        genres: [],
        selectedGenres: []
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
            if(!this.selectedGenres.includes(name)) {
                this.selectedGenres.push(name);
            } else {
                let index = this.selectedGenres.indexOf(name);
                if (index !== -1) {
                    this.selectedGenres.splice(index, 1)
                }
            }

            this.toggleClass(position);
            console.log(this.selectedGenres);
            console.log(this.theme);
        },
        sendData: function () {

            let user = {
                "rut": "1111111",
                "first_name": this.name,
                "last_name": this.lastname,
                "email": this.email,
                "password": this.pwd,
                "list_of_tags": this.selectedGenres
            }

            console.log(user);
            // axios.post('http://localhost:8000/api/users/create', user)
            //     .then(result => {
            //         console.log(result);
            //     })
            //     .catch(error => {
            //         console.log(error);
            //     })   
        },
        getGenres: function () {
            axios.get('http://localhost:8000/api/tags/list-tags')
                .then(res => {
                    console.log(res);
                    if(res.status === 200) {
                        for (let [_, value] of Object.entries(res.data)) {
                            this.genres.push(value["name "]);
                            console.log(value["name "]);
                        }
                    }

                    console.log(this.genres);
                })
                .catch(error => {
                    console.log(error);
            });
        } 
    },
    mounted () {  
        this.getGenres();
        

    //   axios
    //     .get('http://localhost:8000/api/library/list-library')
    //     .then(response => {
    //         this.info = response.data.genres
    //         console.log(response)
    //     }).catch(error => {console.log(error)})
    }
  })
  


