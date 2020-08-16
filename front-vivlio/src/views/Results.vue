<template>
<b-container>
  <b-row>
    <Navbar />
  </b-row>
  <b-row class="results-title">
    <b-col cols="6" sm="8" offset-md="3" md="6" offset-lg="2" lg="8" offset-xl="2" xl="8">
      <h3 class="font-weight-light">Sabemos que buscaste <span style="color: #1C4053; font-size: 35px; font-weight: 600;">{{this.queryBook}}</span> y encontramos: </h3>
    </b-col>
  </b-row>
  <b-row class="main-results">
    <b-col >
      <b-row>
        <b-col>
          hola
        </b-col>
        <b-col>
          hola1
        </b-col>
      </b-row>
    </b-col>
  </b-row>
</b-container>
  <!-- <div class="results">
    <div class="nav-container">
      <div class="wrapper">
        <nav>
          <div class="logo">
            <router-link to="/">
              <img alt="Vue logo" src="@/assets/logo.png" />
            </router-link>
          </div>
          <ul class="nav-items">
            <li>
              <div class="search-box-xss">
                <input
                  type="text"
                  v-model="search"
                  placeholder="¿Qué libro estás buscando?"
                  v-on:keyup.enter="getBook(search)"
                />
              </div>
            </li>
            <li>
              <router-link to="/login">Perfil</router-link>
            </li>
            <li>
              <router-link to="/login">Recomendados</router-link>
            </li>
          </ul>
        </nav>
      </div>
    </div>

    <div class="body-container">
      <div class="search-container">
        <div class="book-container">
          <ul v-for="(book, index) in books" :key="index">
            <li>{{book}}</li>
          </ul>
        </div>
      </div>
    </div>
  </div> -->
</template>

<script>
import { mapState, mapActions } from "vuex";
import Navbar from '@/components/Navbar.vue';

export default {
  name: "Results",
  components: {
    Navbar
  },
  data() {
    return {
      search: "",
      queryBook: "",
    };
  },
  computed: {
    ...mapState(["books"]),
  },
  methods: {
    ...mapActions(["getBook"]),
    getQuery() {
      this.queryBook = this.$attrs.query
    }
  },
  mounted() {
    this.getQuery();
  }
};
</script>

<style scoped>

</style>
