<template>
  <b-container>
    <b-row>
      <Navbar />
    </b-row>
    <!-- Falta añadirle el buscador -->
    <!-- <b-row>
      <b-col cols="12" sm="12" offset-md="3" md="6" offset-lg="2" lg="8" offset-xl="2" xl="8">
        <Seeker />
      </b-col>
    </b-row> -->
    <b-row class="results-title">
      <b-col cols="12" sm="12" offset-md="3" md="6" offset-lg="1" lg="8" offset-xl="0" xl="8">
        <h3 v-if="books.length !== 0" class="font-weight-light">
          Sabemos que buscaste
          <span
            style="color: #1C4053; font-size: 35px; font-weight: 600;"
          >{{query}}</span> y encontramos
          <span>&#x1F9D0;</span>
        </h3>
        <h3 v-if="books.length === 0" class="font-weight-light">
          Sabemos que buscaste
          <span
            style="color: #1C4053; font-size: 35px; font-weight: 600;"
          >{{query}}</span> y ...
        </h3>
      </b-col>
    </b-row>
    <b-row class="main-results">
      <b-col cols="12" sm="12" md="12" lg="12" xl="12">
        <b-row v-if="books !== []">
          <b-col v-for="b in books" :key="b.id" cols="6" sm="6" md="4" lg="4" xl="3">
            <div>
              <b-card :img-src="image" img-top tag="article" style="max-width: 20rem;" class="mb-2">
                <b-card-text>
                  <div class="card-title">
                    <h4>{{b.title}}</h4>
                  </div>
                  <div>Reseña</div>
                </b-card-text>
                <b-button href="#" variant="primary">Comprar</b-button>
              </b-card>
            </div>
          </b-col>
        </b-row>
        <b-row v-if="books.length === 0">
          <div class="results-error">
            <p>
              Pucha, parece que buscaste algo muy extraño, intenta con otro libro
              <span>&#x1F914;</span>
            </p>
          </div>
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
  </div>-->
</template>

<script>
import { mapState, mapActions } from "vuex";
import Navbar from "@/components/Navbar.vue";
import Seeker from "@/components/Seeker.vue";
import imageTest from "@/assets/book.jpeg";

export default {
  name: "Results",
  components: {
    Navbar,
    Seeker,
  },
  data() {
    return {
      search: "",
      queryBook: "",
      image: imageTest,
    };
  },
  computed: {
    ...mapState(["books", "query"]),
  },
  methods: {
    ...mapActions(["getBook"]),
    getQuery() {
      this.queryBook = this.$attrs.query;
    },
  },
  mounted() {
    this.getQuery();
  },
};
</script>

<style scoped>
.main-results {
  margin: 20px auto 100px auto;
  border-radius: 30px;
  padding: 90px 90px;
  background-color: #e2e2e2;
}

.card-title h4 {
  font-weight: 300;
}

.results-error p {
  font-weight: 300;
  font-size: 35px;
}
</style>
