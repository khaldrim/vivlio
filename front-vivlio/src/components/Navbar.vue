<template>
  <div class="navbar-main">
    <b-navbar toggleable="lg">
      <b-navbar-brand href="#">
        <div>
          <router-link to="/">
            <img alt="Vivlio logo" src="@/assets/logo.png" />
          </router-link>
        </div>
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
            <!-- Links for Home Page -->
            <b-nav-item v-if="this.$route.name == 'Home'" class="nav-item-link" to="/signUp">Regístrate</b-nav-item>
            <b-nav-item v-if="this.$route.name == 'Home'" class="nav-item-link" to="/login">Ingresar</b-nav-item>
            
            <!-- Links signUp Page -->
            <b-nav-item v-if="this.$route.name == 'SignUp'" class="nav-item-link" to="/">Inicio</b-nav-item>
            <b-nav-item v-if="this.$route.name == 'SignUp'" class="nav-item-link" to="/login">Ingresar</b-nav-item>

            <!-- Links for Login Page -->
            <b-nav-item v-if="this.$route.name == 'Login'" class="nav-item-link" to="/">Inicio</b-nav-item>
            <b-nav-item v-if="this.$route.name == 'Login'" class="nav-item-link" to="/signUp">Regístrate</b-nav-item>

            <!-- Links for Results Page -->
            <!-- TODO: Falta controlar el estado de logeo :) -->
             <b-nav-form v-if="this.$route.name == 'Results'">
                <b-form-input size="sm" class="mr-sm-2" placeholder="Busca otro libro"></b-form-input>
                <!-- TODO: Cambiar por un icono mejor! -->
                <b-button size="sm" class="my-2 my-sm-0" type="submit">Buscar</b-button>
            </b-nav-form>
            <b-nav-item v-if="this.$route.name == 'Results'" class="nav-item-link" to="/signUp">Regístrate</b-nav-item>
            <b-nav-item v-if="this.$route.name == 'Results'" class="nav-item-link" to="/login">Ingresar</b-nav-item>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
.navbar-main {
    margin: 3% auto;
    width: 100%;
}

.nav-item-link{
    font-weight: 350;
    font-size: 30px;
}
</style>