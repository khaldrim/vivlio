<template>
  <b-container>
    <b-row>
      <Navbar />
    </b-row>
    <!-- <b-row class="book-title">
      <b-col cols="12" sm="12" offset-md="3" md="6" offset-lg="1" lg="8" offset-xl="0" xl="8">
        <h3>Detalle de tu libro</h3>
      </b-col>
    </b-row> -->
    <b-row class="main-results">
      <b-row>
        <b-col cols="3" sm="3" md="3" lg="3" xl="3">
          <b-img :src="image" fluid alt="Portada" width="250"></b-img>
        </b-col>
        <b-col cols="6" sm="6" md="6" lg="6" xl="6">
          <b-row>
            <b-col cols="12" sm="12" md="12" lg="12" xl="12">
              <h5>
                Título: Guía del autoestopista intergaláctico
              </h5>
            </b-col>
            <b-col cols="12" sm="12" md="12" lg="12" xl="12">
              <h5>
                Autor(es): Adam Douglas
              </h5>
            </b-col>
            <b-col cols="12" sm="12" md="12" lg="12" xl="12">
              <h5>Sinopsis:</h5>
              <p>
                Un jueves a la hora de comer, la Tierra es demolida para poder construir una nueva autopista hiperespacial. Arthur Dent, un tipo que esa misma mañana ha visto cómo echaban abajo su propia casa, considera que eso supera lo que una persona puede soportar. Arthur huirá de la Tierra junto a un amigo suyo, Ford Prefect, que resultará ser un extraterrestre emparentado con Zaphod Beeblebrox, un pirata esquizoide de dos cabezas, en cuya nave conocerá al resto de personajes que lo acompañarán: un androide paranoide y una terrícola que, como él, ha logrado escapar. Douglas Adams fue el creador de toda una serie de manifestaciones de la Guía del autoestopista galáctico: primero fue novela radiofónica, luego se convirtió en libro, series televisivas y teatrales, un juego de ordenador, cómics y toallas de baño. La película ascendió hasta las cumbres de la producción cinematográfica. Esta edición cuenta con entrevistas y materiales a partir del rodaje de la misma.
              </p>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="12" sm="12" md="12" lg="12" xl="12">
          <hr size="50">
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="12" sm="12" md="12" lg="12" xl="12">
          <h5><b>Compralo en</b></h5>
        </b-col>
        <!-- FDL -->
         <b-col cols="4">
           <div class="logo-tienda">
             <b-img :src="imageFDL" fluid alt="Portada" width="250"></b-img>
           </div>
        </b-col>
         <b-col cols="4">
           <div class="price">
             <p>$7.990</p>
           </div>
        </b-col>
        <b-col cols="4">
          <b-btn class="buy">Comprar</b-btn>
        </b-col>

        <!-- Buscalibre -->
         <b-col cols="4">
           <div class="logo-tienda">
             <b-img :src="imageBL" fluid alt="Portada" width="250"></b-img>
           </div>
        </b-col>
         <b-col cols="4">
           <div class="price">
             <p>$12.990</p>
           </div>
        </b-col>
        <b-col cols="4">
          <b-btn class="buy">Comprar</b-btn>
        </b-col>
      </b-row>

      <!-- Opiniones -->
      <b-row>

      </b-row>
    </b-row>
  </b-container>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import imageTest from "@/assets/book.jpeg";
import imageFDL from "@/assets/fcdl_logo.png";
import imageBL from "@/assets/buscalibre.png";


export default {
  name: "Book",
  components: {
    Navbar,
  },
  data() {
    return {
      search: "",
      queryBook: "",
      image: imageTest,
      imageFDL: imageFDL,
      imageBL: imageBL
    };
  },
  methods: {
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

hr.divider {
  /* margin-top: 1rem; */
  /* margin-bottom: 1rem; */
  /* border: 0; */
  /* border-top: 1px solid rgba(19, 64, 84, 0.1); */
  border-top: 1px solid #8c8b8b;
}

h5 {
  margin: 20px 0px;
  color: #134054;
}

.logo-tienda {
  margin: 15px 0px;
}

.price {
  color: rgb(40, 97, 40);
  font-size: 30px;
  margin: 15px 30px;
}

.buy {
  margin: 20px 0px;
  background-color: #134054;
}
</style>
