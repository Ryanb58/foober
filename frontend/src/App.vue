<template>
  <div id="app">

    <section class="section">
      <router-view></router-view>
    </section>
    <div class="container">
      <div class="notification">
        This container is <strong>centered</strong> on desktop.
      </div>
    </div>
  </div>
</template>
<script>
import Index from './components/Index.vue'

export default {
  name: 'app',
  components: {
    Index
  }
}
</script>

<style lang="scss">
// Import Bulma's core
@import "~bulma/sass/utilities/_all";

// Set your colors
$primary: #cc580a;
$primary-invert: findColorInvert($primary);
$secondary: #d48d66;
$secondary-invert: findColorInvert($primary);
$dark: #1b1e1c;
$dark-invert: findColorInvert($primary);
$medium: #424743;
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

