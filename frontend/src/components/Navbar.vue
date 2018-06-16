<template>
  <nav class="navbar is-medium" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <!-- navbar items, navbar burger... -->
      <router-link class="navbar-item" to="/" active-class="active">
        <!-- <img src="https://bulma.io/images/bulma-logo.png" alt="Bulma: a modern CSS framework based on Flexbox" width="112" height="28"> -->
        Foober
      </router-link>
    </div>
    <div class="navbar-menu">
      <!-- navbar start, navbar end -->
      <div class="navbar-start">
        <router-link class="navbar-item" to="/food" active-class="active">
          Food
        </router-link>
      </div>
      <div class="navbar-end">
        <div v-if="loggedIn" class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link" href="/profile">
            Ryanb58
          </a>
          <div class="navbar-dropdown is-boxed">
            <a class="navbar-item" href="/settings">
              Settings
            </a>
            <a class="navbar-item" href="/about">
              About
            </a>
            <router-link class="navbar-item" to="/logout" active-class="active">
              Log Out
            </router-link>
            <hr class="navbar-divider">
            <a class="navbar-item" href="/about">
              About
            </a>
          </div>
        </div>
        <router-link v-else class="navbar-item" to="/login" active-class="active">
          Login
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import auth from './../utils/auth.js'

export default {
  name: "Navbar",
  data() {
    return {
      loggedIn: auth.loggedIn(),
    };
  },
  created () {
    auth.onChange = loggedIn => {
      this.loggedIn = loggedIn
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
