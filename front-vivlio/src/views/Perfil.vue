<template>
  <b-container>
    <b-row>
      <Navbar />
    </b-row>
    <b-row class="signup-form-title">
      <b-col cols="12" sm="12" offset-md="3" md="6" offset-lg="3" lg="6" offset-xl="3" xl="6">
        <h1 class="profile-title">Usuario</h1>
      </b-col>
    </b-row>
    <b-row class="signup-form-group-input">
      <b-col cols="12" sm="12" offset-md="3" md="6" offset-lg="3" lg="6" offset-xl="3" xl="6">
        helo
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import axios from "axios";
export default {
  name: "Perfil",
  components: {
    Navbar,
  },
  data() {
    return {
      email: "EmailPrueba8@prueba.cl",
      user: {}
    };
  },
  methods: {
    getUsuario: function () {
      console.log("getUsuario");
      axios
        .get(process.env.VUE_APP_API_URL + "/api/users/get", {
          params: this.email
        
        }
        )
        .then((res) => {
          if (res.status === 200) {
            this.user = res.data
          }

          console.log(this.user);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.getUsuario();
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
