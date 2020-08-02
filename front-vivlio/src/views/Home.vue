<template>
  <div class="home">
    <div id="nav" class="nav-container">
      <div class="wrapper">
        <nav>
          <div class="logo">
            <router-link to="/">
            <img alt="Vue logo" src="@/assets/logo.png">
            </router-link>
          </div>
          <ul class="nav-items">
            <li><router-link to="/signUp">Regístrate</router-link></li>
            <li><router-link to="/login">Ingresar</router-link></li>
         </ul>
        </nav>
      </div>
    </div>

    <Seeker/>

  </div>
</template>

<script>
// @ is an alias to /src
import Seeker from '@/components/Seeker.vue'

export default {
  name: 'Home',
  components: {
    Seeker
  }
}

</script>
