<template>
  <b-container>
    <b-row>
      <Navbar />
    </b-row>
    <b-row class="home-title">
      <b-col cols="6" sm="8" offset-md="3" md="6" offset-lg="2" lg="8" offset-xl="2" xl="8">
        <h3 class="font-weight-light">Encuentra tu próximo libro favorito</h3>
      </b-col>
    </b-row>
    <b-row class="seeker">
      <b-col cols="6" sm="8" offset-md="3" md="6" offset-lg="2" lg="8" offset-xl="2" xl="8">
        <Seeker/>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
// @ is an alias to /src
import Seeker from '@/components/Seeker.vue'
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'Home',
  components: {
    Seeker,
    Navbar
  }
}

</script>


<style scoped>
.home-title {
  margin: 5% auto 0 auto;
  font-weight: 150;
}

.seeker {
  margin: 5% auto;
}
</style>
