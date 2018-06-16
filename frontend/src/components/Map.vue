<template>
  <section class="container">
    <iframe
    width="900"
    height="800"
    frameborder="0" style="border:0"
    src="https://www.google.com/maps/embed/v1/place?key=AIzaSyDhcT1fMRMZ_Bl2ke67gzQtQiicr75DeFA
        &q=Indianapolis, IN" allowfullscreen>
    </iframe>
    <a href="https://drive.google.com/a/smartfile.com/open?id=1mw3vWBsvcEtdws9cE25rHKHaawwezNsR&usp=sharing" target="_blank">Display in Google Maps</a>
  </section>
</template>

<script>
import auth from "./../utils/auth.js";

export default {
  name: "Map"
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
