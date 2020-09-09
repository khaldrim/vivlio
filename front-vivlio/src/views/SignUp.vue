<template>
  <b-container>
    <b-row>
      <Navbar />
    </b-row>
    <b-row class="signup-form-title">
      <b-col cols="12" sm="12" offset-md="3" md="6" offset-lg="3" lg="6" offset-xl="3" xl="6">
        <h1 class="profile-title">Bienvenido a Vivlio</h1>
      </b-col>
    </b-row>
    <b-row class="signup-form-group-input">
      <b-col cols="12" sm="12" offset-md="3" md="6" offset-lg="3" lg="6" offset-xl="3" xl="6">
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
          <!-- Email -->
          <b-form-group class="signup-form-input" id="input-group-1" label="Email:" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="form.email"
              type="email"
              required
              placeholder="Ingresa tu correo"
            ></b-form-input>
          </b-form-group>

          <!-- Names -->
          <b-form-group class="signup-form-input" id="input-group-2" label="Nombres:" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.name"
              required
              placeholder="Ingresa tus Nombres"
            ></b-form-input>
          </b-form-group>

          <!-- LastName -->
          <b-form-group class="signup-form-input" id="input-group-3" label="Apellidos:" label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="form.lastname"
              required
              placeholder="Ingresa tus Apellidos"
            ></b-form-input>
          </b-form-group>

          <!-- Password -->
          <b-form-group class="signup-form-input" id="input-group-4" label="Contraseña: " label-for="input-4">
            <b-input
              type="password"
              id="text-password"
              aria-describedby="password-help-block"
              v-model="form.pwd"
            ></b-input>
          </b-form-group>

          <b-form-group class="signup-form-input" id="input-group-5" label="Indícanos tus preferencias: " label-for="input-5">
            <div v-for="(genre,index) in genres" :key="index">
              <label class="preference-label" for="index">{{genre}}: {{form.preferences[index]}}%</label>
              <b-input
                class="form-input-range"
                type="range"
                min="1"
                max="100"
                value="10"
                step="1"
                v-model="form.preferences[index]"
              ></b-input>
            </div>
          </b-form-group>

          <div class="send-form">
            <b-button type="submit" class="signup-form-input-btn" variant="primary">Registrarte</b-button>
          </div>
          <div class="send-form">
            <b-button type="reset" class="signup-form-input-btn"  variant="danger">Limpiar</b-button>
          </div>
        </b-form>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import axios from "axios";
export default {
  name: "SignUp",
  components: {
    Navbar,
  },
  data() {
    return {
      form: {
        email: "",
        name: "",
        lastname: "",
        pwd: "",
        preferences: [],
      },
      show: true,
      genres: []
    };
  },
  methods: {
    onSubmit() {
      console.log("Submited.");
      let user = {
        first_name: this.form.name,
        last_name: this.form.lastname,
        email: this.form.email,
        password: this.form.pwd,
        preferences: this.form.preferences,
      };

      console.log(user);
      console.log("Send to backend!");
      axios
        .post(process.env.VUE_APP_API_URL + "/api/users/create", user)
        .then((result) => {
          console.log(result);
          console.log("Registro exitoso.");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    onReset() {
      this.form.name = "";
      this.form.lastname = "";
      this.form.email = "";
      this.form.pwd = "";

      for (let index = 0; index < this.form.preferences.length; index++) {
        this.form.preferences[index] = "50";
      }
    },
    getGenres: function () {
      console.log("getGenres");
      axios
        .get(process.env.VUE_APP_API_URL + "/api/tags/list-tags")
        .then((res) => {
          console.log(res);
          if (res.status === 200) {
            for (let [_, value] of Object.entries(res.data)) {
              this.genres.push(value["name "]);
              this.form.preferences.push("50");
            }
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.getGenres();
  },
};
</script>

<style scoped>
.signup-form-title {
  color: #1C4053;
  margin: 50px auto;
}

.signup-form-group-input {
  border-radius: 25px;
  width: 80%;
  background-color: #f1f1f1;
  color: #1C4053;
  margin: 0px auto 100px auto;
}

.signup-form-input {
  margin: 10% auto;
  font-size: 25px;
}

.signup-form-input-btn {
  font-size: 25px;
  margin: 5% auto;
} 

.send-form {
  margin: 5% 5px;
  text-align: center;
}
</style>