<template>
  <div id="app">
    <Navbar></Navbar>
    <section class="section">
      <router-view></router-view>
    </section>
    <Footer></Footer>
  </div>
</template>


<script>
import Login from "./components/Login.vue";
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
import Index from "./components/Index.vue";
import FoodList from "./components/FoodList.vue";
import FoodAddEdit from "./components/FoodList.vue";
import Map from "./components/Map.vue";

import auth from './utils/auth.js'

export default {
  name: "app",
  data() {
    return {
      activeIndex: '1',
      activeIndex2: '1',
      loggedIn: auth.loggedIn(),
    };
  },
  created () {
    auth.onChange = loggedIn => {
      this.loggedIn = loggedIn
    }
  },
  components: {
    FoodAddEdit,
    FoodList,
    Index,
    Login,
    Navbar,
    Footer,
    Map,
  }
};
</script>

<style lang="scss">
// Import Bulma's core
@import "~bulma/sass/utilities/_all";

// Set your colors
$primary: #EC7964;
$primary-invert: findColorInvert($primary);
$secondary: #F0A480;
$secondary-invert: findColorInvert($primary);
$dark: #1b1e1c;
$dark-invert: findColorInvert($primary);
$medium: #6DC1AF;
$medium-invert: findColorInvert($primary);
$light: #9ea39f;
$light-invert: findColorInvert($primary);

// Setup $colors to use as bulma classes (e.g. 'is-twitter')
$colors: (
    "white": ($white, $black),
    "black": ($black, $white),
    "light": ($light, $light-invert),
    "dark": ($dark, $dark-invert),
    "primary": ($primary, $primary-invert),
    "info": ($info, $info-invert),
    "success": ($success, $success-invert),
    "warning": ($warning, $warning-invert),
    "danger": ($danger, $danger-invert),
    "secondary": ($secondary, $secondary-invert),
    "medium": ($medium, $medium-invert),
);

// Links
$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>
