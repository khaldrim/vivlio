<template>
  <div class="signUp">
    <Navbar />

    <div class="body-container">
      <div class="profile-container">
        <h1 class="profile-title">Bienvenido a Vivlio</h1>
        <div class="profile-form">
          <div class="profile-title-input">
            <p>Nombre</p>
          </div>
          <div class="profile-input">
            <input id="name" v-model="name" type="text" placeholder="Juan">
          </div>

          <div class="profile-title-input">
            <p>Apellido</p>
          </div>
          <div class="profile-input">
            <input id="lastname" v-model="lastname" type="text" placeholder="Pérez">
          </div>
          
          <div class="profile-title-input">
            <p>Email</p>
          </div>
          <div class="profile-input">
            <input id="email" v-model="email" type="email" placeholder="juan.perez@email.com">
          </div>
          
          
          <div class="profile-title-input">
            <p>Contraseña</p>
          </div>
          <div class="profile-input">
            <input id="pwd" v-model="pwd" type="password" placeholder="***********">
          </div>
          
          <div class="profile-genre-title">
            <p>Indicanos tus preferencias de géneros literarios,<br/> de 1 (poco) a 100 (mucho):</p>
          </div> 

          <div class="preferences">
            <div class="preference" v-for="(genre,index) in genres" :key=index>
              <label class="preference-label" for=index>{{genre}}: {{preferences[index]}}%</label>
              <input class="preference-range" v-model="preferences[index]" id="index" type="range" min="1" value="10" step="1" max="100" />
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
  import Navbar from '@/components/Navbar.vue'
  import axios from 'axios'
  export default{
    name: 'SignUp',
    components: {
      Navbar
    },
    data(){
      return {
       theme: ['profile-genre', 'profile-genre', 'profile-genre', 'profile-genre', 'profile-genre', 'profile-genre', 'profile-genre'],
       isActive: [false, false, false, false, false, false, false],
       name: "",
       lastname: "",
       email: "",
       pwd: "",
       genres: [],
       preferences: [],
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
                "preferences": this.preferences
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
            axios.get('http://0.0.0.0:8000/api/tags/list-tags')
                .then(res => {
                    console.log(res);
                    if(res.status === 200) {
                        for (let [_, value] of Object.entries(res.data)) {
                            this.genres.push(value["name "]);
                            this.preferences.push("50");
                        }
                    }
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

<style scoped>
  input[type=text], select {
    width: 81%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
  }
  
  input[type=email], select {
    width: 81%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
  }

  input[type=password], select {
    width: 81%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
  }
  
  .preferences {
    color: #1C4053;
    width: 75%;
    margin: 0 auto;
    align-content: center;
    font-size: 25px;
    background-color: #f1f1f1;
  }

  .preference {
    margin: 5% 5%;
  }

  .preference-label {
    padding-right: 40px;
    text-align: start;
    font-weight: 300;
    width: 100%;
  }
  
  .preference-range {
    background-color: #f1f1f1;
  }

  input[type=range] {
    height: 26px;
    -webkit-appearance: none;
    margin: 10px 0;
    width: 100%;
  }

  input[type=range]:focus {
    outline: none;
  }

  input[type=range]::-moz-range-track {
    width: 100%;
    height: 4px;
    cursor: pointer;
    animate: 0.2s;
    box-shadow: 1px 1px 1px #000000;
    background: #1C4053;
    border-radius: 4px;
    border: 1px solid #000000;
  }
  
  input[type=range]::-moz-range-thumb {
    box-shadow: 1px 1px 1px #1C4053;
    border: 3px solid #1C4053;
    height: 16px;
    width: 16px;
    border-radius: 16px;
    background: #fff;
    cursor: pointer;
  }

</style>