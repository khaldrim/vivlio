<template>
  <div class="signUp">
    <div class="nav-container">
      <div class="wrapper">
        <nav>
          <div class="logo">
            <router-link to="/">
            <img alt="Vue logo" src="@/assets/logo.png">
            </router-link>
          </div>
          <ul class="nav-items">
            <li><router-link to="/login">Ingresar</router-link></li>
         </ul>
        </nav>
      </div>
    </div>

    <div class="body-container">
            <div class="profile-container">
                <h1 class="profile-title">Bienvenido a Vivlio</h1>
                <div class="profile-form">
                    <div class="profile-title-input">
                      <p>Nombre</p>
                    </div>
                    <div class="profile-input">
                      <input id="name" v-model="name" type="text" placeholder="   Juan">
                    </div>
                    <div class="profile-title-input">
                      <p>Apellido</p>
                    </div>
                    <div class="profile-input">
                      <input id="lastname" v-model="lastname" type="text" placeholder="   Pérez">
                    </div>
                    <div class="profile-title-input">
                      <p>Email</p>
                    </div>
                    <div class="profile-input">
                      <input id="email" v-model="email" type="email" placeholder="   juan.perez@email.com">
                    </div>
                    <div class="profile-title-input">
                      <p>Contraseña</p>
                    </div>
                    <div class="profile-input">
                      <input id="pwd" v-model="pwd" type="password" placeholder="   ***********">
                    </div>
                    <div class="profile-genre-title">
                      <p>Selecciona cuáles son los géneros literarios que <br>más te gustan:</p>
                    </div>

                    <div class="profile-genre-all">
                      <div v-for="(genre,index) in genres">
                        <div v-on:click="addGenre(genre, index)" v-if="!isActive[index]" class="profile-genre">
                          <p>{{genre}}</p>
                        </div>
                        <div v-on:click="addGenre(genre, index)" v-else class="profile-genre-selected">
                          <p>{{genre}}</p>
                        </div>
                      </div>
                    </div>

                    <div class="profile-submit">
                      <button v-on:click="sendData()">Registrarse</button>
                    </div>

                </div>
            </div>
        </div>
      </div>
</template>

<script>


  import axios from 'axios'
  export default{
    data(){
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
    methods:{
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
            axios.get('http://192.168.99.100:8000/api/tags/list-tags')
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
  }
 }

</script>
