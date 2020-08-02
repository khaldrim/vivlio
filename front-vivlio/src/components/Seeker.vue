<template>
  <div class="search-container">
      <div class="search-box">
        <input type="text" v-model="search" placeholder="¿Qué libro estás buscando?">
        <router-link to="/results">
        <button @click="getBook(search)">Buscar</button>
        </router-link>
      </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapMutations, mapActions } from "vuex";

export default {
  name: 'Seeker',
  data(){
    return {
      search:''
    }
  },
  methods:{
    //...mapMutations(['bookTitle']),
    ...mapActions(['getBook'])
  }

}

</script>
