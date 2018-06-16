<template>
  <div class="index">
    <div class="tile is-ancestor">
      <div class="tile is-vertical is-8">
        <div class="tile">
          <div class="tile is-parent is-vertical">
            <article class="tile is-child notification is-primary">
              <p class="title">Helping the Community</p>
              <p class="subtitle">Indianapolis is around 21% insecure according to Gleaners. Help us provide for the community by donating your food that is past it's `sell by date`.</p>
            </article>
            <article class="tile is-child notification is-warning">
              <p class="title">Educate & Participate</p>
              <p class="subtitle"><a href="https://www.gleaners.org/hunger101/community/" target="_blank">Click here to learn how your community is fighting hunger and how you can help.</a></p>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child notification is-info">
              <p class="title">Helping Hands</p>
              <p class="subtitle">Stigma Free Food</p>
              <figure class="image is-4by3">
                <img src="https://www.gleaners.org/wp-content/uploads/2014/12/fooddrives.jpg">
                <!-- <img :src="'../assets/dashboard-banner.jpg'"> -->
              </figure>
            </article>
          </div>
        </div>
        <div class="tile is-parent">
          <article class="tile is-child notification is-danger">
            <p class="title">Motivation</p>
            <p class="subtitle">"It always seems impossible until it is done."<br /> - Nelson Mandela</p>
            <div class="content">
              <!-- Content -->
            </div>
          </article>
        </div>
      </div>
      <div class="tile is-parent">
        <article class="tile is-child notification is-success">
          <div class="content">
            <p class="title">Information</p>
            <p class="subtitle">
              <ul>
                <li>
                  Over 75% of client households report having to choose between paying for food and paying for transportation, medical care, or utilities.
                </li>
                <li>
                  65% report having to choose between paying for food and paying for housing.
                </li>
                <li>
                  41% of households report having to choose between paying for food and paying for educational expenses.
                </li>
                <li>70% of client households are living at or below 100% of the poverty level.</li>
                <li>53% of client households report annual income of $10,000 and under.</li>
                <li>64% of client households report at least one employed person at some point in the past year.</li>
                <li>29% of client households include grandparents who have responsibility for grandchildren who live with them – which can be a potential barrier to employment for those households.</li>
              </ul>
            </p>
            <div class="content">
              <!-- Content -->
              <a href="https://www.gleaners.org/hunger101/indiana/" target="_blank">Source: Gleaners</a>
            </div>
          </div>
        </article>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Index"
  // props: {
  //   msg: String
  // }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
