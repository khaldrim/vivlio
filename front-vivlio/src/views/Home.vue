<template>
  <div class="home">
    <Navbar />
    <Seeker/>
  </div>
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
  
</style>
