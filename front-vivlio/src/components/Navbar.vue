<template>
    <div id="nav" class="nav-container">
        <div class="wrapper">
            <nav>
                <div class="logo">
                    <router-link to="/">
                        <img alt="Vivlio logo" src="@/assets/logo.png" />
                    </router-link>
                </div>
                
                <!-- Links for Home page -->
                <div v-if="this.$route.name ==  'Home'">
                    <ul class="nav-items">
                        <li><router-link to="/signUp">Regístrate</router-link></li>
                        <li><router-link to="/login">Ingresar</router-link></li>
                    </ul>
                </div>

                <!-- Links for Signup page -->
                <div v-if="this.$route.name ==  'SignUp'">
                    <ul class="nav-items">
                        <li><router-link to="/">Inicio</router-link></li>
                        <li><router-link to="/login">Ingresar</router-link></li>
                    </ul>
                </div>

            </nav>
        </div>
    </div>
</template>

<script>
export default {
    name: "Navbar",
};
</script>

<style scoped>
    .nav-items li a {
        text-decoration: none;
        font-size: 25px;
        color: #1c4053;
    }
</style>