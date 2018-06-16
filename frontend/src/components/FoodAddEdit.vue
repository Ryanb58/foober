<template>
  <section>
    <div class="field">
      <b-field label="Location">
        <b-autocomplete
          v-model="form.location"
          :data="data"
          placeholder="address"
          field="title"
          :loading="isFetching"
          @input="getAsyncData"
          @select="setSelectedLocation">

          <template slot-scope="props">
              <div class="media">
                  <div class="media-left">
                    {{ props.option.address }} - {{ props.option.city }}
                  </div>
              </div>
          </template>
        </b-autocomplete>
      </b-field>
    </div>

    <div class="field">
      <label class="label">Name</label>
      <div class="control">
        <input type="text" v-model="form.name" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Contact</label>
      <div class="control">
        <input type="text" v-model="form.contact_name" class="input" />
      </div>
    </div>
    <!-- <div class="field">
      <label class="label">Available</label>
      <div class="control">
        <input type="text" v-model="form.available_timestamp" class="input" />
      </div>
    </div> -->
    <b-field label="Select a date">
        <b-datepicker
            placeholder="Click to select..."
            icon="calendar-today"
            v-model="form.available_date">
        </b-datepicker>
    </b-field>
    <section>
      <b-field label="Select time">
        <b-timepicker
          rounded
          placeholder="Click to select..."
          icon="clock"
          :hour-format="format"
          :v-model="form.available_time">
          <button class="button is-primary"
            @click="form.available_time = new Date()">
            <b-icon icon="clock"></b-icon>
            <span>Now</span>
          </button>

          <button class="button is-danger"
              @click="form.available_time = null">
              <b-icon icon="close"></b-icon>
              <span>Clear</span>
          </button>
        </b-timepicker>
      </b-field>
    </section>
    <div class="field">
      <b-field label="Type">
        <b-select placeholder="Select a type" v-model="form.type">
          <option
              v-for="type in types"
              :value="type.value"
              :key="type.value">
              {{ type.display_name }}
          </option>
        </b-select>
      </b-field>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link" v-on:click="saveClick()">Submit</button>
      </div>
      <div class="control">
        <router-link class="button is-text" to="/food">
          Cancel
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "FoodAddEdit",
  data() {
    return {
      types: {},
      locations: {},
      data: [],
      seller_name: "",
      selected: null,
      isFetching: false,
      form: {
        id: "",
        name: "",
        contact_name: "",
        available_time: this.$moment().toDate(),
        available_date: this.$moment().toDate(),
        available_timestamp: this.$moment().toDate(),
        type: "",
        location: ""
      }
    };
  },
  created: function() {
    var _this = this;

    // Load extra info from OPTIONS request.
    _this
      .$http({
        url: "/api/food/v1/item/",
        method: "OPTIONS"
      })
      .then(function(data) {
        _this.types = data.data.actions.POST.type.choices;
      });

    var id = _this.$route.params.id;

    // Load acquisition.
    if (id != undefined) {
      _this
        .$http({
          url: "/api/food/v1/item/" + id + "/",
          method: "GET"
        })
        .then(function(data) {
          data = data.data;
          _this.form.id = data.id;
          _this.form.name = data.name;
          _this.form.contact_name = data.contact_name;
          _this.form.available_timestamp = _this.$moment(
            data.available_timestamp
          );
          _this.form.available_time = _this.$moment(data.available_timestamp);
          _this.form.available_date = _this
            .$moment(data.available_timestamp)
            .toDate();
          _this.form.type = data.type;
          _this.form.location = data.location;
        });
    }
  },
  methods: {
    // You have to install and import debounce to use it,
    // it's not mandatory though.
    getAsyncData: function() {
      this.data = [];
      this.isFetching = true;
      this.$http
        .get(`/api/food/v1/location/?search=${this.seller_name}`)
        .then(({ data }) => {
          data.results.forEach(item => this.data.push(item));
          this.isFetching = false;
        })
        .catch(error => {
          this.isFetching = false;
          throw error;
        });
    },
    setSelectedLocation: function(option) {
      this.selected = option;
      this.form.location = option.id;
    },
    saveClick: function() {
      var _this = this;
      //Save acquisition.
      var url;
      var item_id = this.$route.params.id;
      var is_add = item_id === undefined;
      if (is_add) {
        url = "/api/food/v1/item/";
      } else {
        url = "/api/food/v1/item/" + _this.form.id + "/";
      }

      // Clone state dict and then remove `errors` key.
      let data = JSON.stringify(_this.state);
      data = JSON.parse(data);
      delete data.errors;
      // data["available_timestamp"] =
      // data["available_date"] + data["available_time"];
      data["available_timestamp"] = _this
        .$moment(
          data["available_date"].format("L") +
            data["available_time"].format("hh:mm:ss a")
        )
        .unix();

      this.$http({
        url: url,
        method: is_add ? "POST" : "PATCH",
        data: data
      }).then(function() {
        // Let the user know we saved the acquisition.
        _this.$snackbar.open({
          message: "Saved!",
          type: "is-success"
        });

        window.location.href = "#/food";
      });
    }
  },
  computed: {
    format() {
      return "12";
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
