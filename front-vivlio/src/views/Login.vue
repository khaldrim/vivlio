<template>
   <b-container>
    <b-row>
      <Navbar />
    </b-row>
    <b-row class="login-form-title">
      <b-col cols="12" sm="12" offset-md="3" md="6" offset-lg="4" lg="6" offset-xl="3" xl="6">
        <h1>Ingresa a Vivlio!</h1>
      </b-col>
    </b-row>
    <b-row>
      <b-col cols="12" sm="12" offset-md="3" md="6" offset-lg="4" lg="6" offset-xl="3" xl="6">
         <b-form @submit="onSubmit" v-if="show">
          <!-- Email -->
          <b-form-group class="login-form-input" id="input-group-1" label="Email:" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="form.email"
              type="email"
              required
              placeholder="Ingresa tu correo"
            ></b-form-input>
          </b-form-group>

          <!-- Password -->
          <b-form-group class="login-form-input" id="input-group-4" label="Contraseña: " label-for="input-4">
            <b-input
              type="password"
              id="text-password"
              aria-describedby="password-help-block"
              required
              v-model="form.pwd"
            ></b-input>
          </b-form-group>

          <div class="send-form">
            <b-button type="submit" class="login-form-input-btn" variant="primary">Ingresar</b-button>
          </div>
         </b-form>
      </b-col>
    </b-row>
   </b-container>
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'Login',
  components: {
    Navbar
  },
  data() {
    return {
      show: true,
      form: {
        email: '',
        pwd: ''
      }
    }
  },
  methods: {
    onSubmit() {
      console.log("Login.");
    }
  }
}
</script>

<style scoped>
.login-form-title {
  color: #1C4053;
  margin: 50px auto;
}

.login-form-input {
  margin: 5% auto;
  font-size: 25px;
}

.login-form-input-btn {
  font-size: 20px;
}

.login-input {
  margin: auto;
  width: 100%;
  height: 100%;
  background: #ffffff;
}

.login-input input {
  margin: 5px auto;
  width: 300px;
  height: 40px;
  border: 2px solid #1C4053;
  box-sizing: border-box;
  border-radius: 30px;
  box-shadow: none;
  align-content: center;
  text-decoration: none;
  text-indent: 1cm;
  color: #1C4053;
  font-weight: 600;
  background: #F4F4F4;

}

.login-input button {
  margin: 5px 85px;
  width: 120px;
  height: 40px;
  border: 2px solid #1C4053;
  box-sizing: border-box;
  border-radius: 30px;
  box-shadow: none;
  align-content: center;
  text-decoration: none;
  color: #F4F4F4;
  font-weight: 600;
  background: #1C4053;

}

input:focus, button:focus, textarea:focus, select:focus{
  outline: none;
}
</style>