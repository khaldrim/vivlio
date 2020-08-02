<template>
  <div class="login">
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
         </ul>
        </nav>
      </div>
    </div>

    <div class="login-container">
      <div class="login-input">
        <input type="email" placeholder="Ingresa tu correo" />
        <input type="password" placeholder="*********" />
        <router-link to= "location.href='https\://www.google.cl'">
          <button type="button">Ingresar</button>
        </router-link>
      </div>
    </div>

  </div>
</template>
