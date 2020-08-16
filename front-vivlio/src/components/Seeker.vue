<template>
  <div class="search-box">
    <div>
      <input
        type="text"
        v-model="search"
        v-on:keyup.enter="onEnter"
        placeholder="¿Qué libro estás buscando?"
      />
    </div>
    <div class="search-button-div">
      <b-button class="search-button" variant="outline-primary" @click="getBook(search)">Buscar</b-button>
    </div>
  </div>

  <!-- <div class="search-container">
      <div class="search-box">
        <input type="text" v-model="search" placeholder="¿Qué libro estás buscando?">
        <router-link to="/results">
        <button @click="getBook(search)">Buscar</button>
        </router-link>
      </div>
  </div>-->
</template>

<script>
import axios from "axios";
import { mapMutations, mapActions } from "vuex";

export default {
  name: "Seeker",
  data() {
    return {
      search: "",
    };
  },
  methods: {
    //...mapMutations(['bookTitle']),
    ...mapActions(["getBook"]),
    onEnter() {
      this.$router.push({ path: 'results', query: { book: this.search }});
    },
  },
};
</script>

<style scoped>
input[type="text"] {
  margin: 0 auto;
  width: 700px;
  height: 60px;
  background-color: #f9f9f9;
  border: 2px solid #1c4053;
  box-sizing: border-box;
  border-radius: 30px;
  align-content: center;
  font-size: 25px;
  padding-left: 50px;
}

input:focus,
textarea:focus,
select:focus {
  outline: none;
  box-shadow: 0 0 5px #224f68;
  padding: 3px 0px 3px 3px;
  border: 1px solid #3989b4;
  padding-left: 50px;
}

.search-button-div {
  margin: 5% auto;
  font-size: 25px;
  text-align: center;
}

.search-button {
  color: #fff !important;
  background-color: #1C4053 !important;
  border-color: #1C4053 !important;
  font-size: 25px;
  width: 120px;
  border-radius: 25px;
}
</style>