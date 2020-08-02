<template>
  <div class="results">
    <div class="nav-container">
      <div class="wrapper">
        <nav>
          <div class="logo">
            <router-link to="/">
            <img alt="Vue logo" src="@/assets/logo.png">
            </router-link>
          </div>
          <ul class="nav-items">
            <li><router-link to="/login">Ingresar</router-link></li>
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

  </div>
</template>

<script>
  import { mapState } from "vuex";
  export default{
    data(){
      return{
      }
    },
    computed:{
      ...mapState(['books'])
    }
  }

</script>
