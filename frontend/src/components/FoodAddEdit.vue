<template>
  <section>
    <div class="field">
      <b-field label="Seller">
        <b-autocomplete
          v-model="seller_name"
          :data="data"
          placeholder="e.g. Custom Jewel"
          field="title"
          :loading="isFetching"
          @input="getAsyncData"
          @select="setSelectedSeller">

          <template slot-scope="props">
              <div class="media">
                  <div class="media-left">
                    {{ props.option.license_name }} - {{ props.option.business_name }}
                  </div>
              </div>
          </template>
        </b-autocomplete>
      </b-field>
    </div>

    <div class="field">
      <label class="label">Business Name</label>
      <div class="control">
        <input type="text" v-model="form.business_name" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">License name</label>
      <div class="control">
        <input type="text" v-model="form.license_name" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">License Number</label>
      <div class="control">
        <input type="text" v-model="form.license_name" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Permise Street</label>
      <div class="control">
        <input type="text" v-model="form.premise_street" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Permise City</label>
      <div class="control">
        <input type="text" v-model="form.premise_city" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Permise State</label>
      <div class="control">
        <input type="text" v-model="form.premise_state" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Permise Zipcode</label>
      <div class="control">
        <input type="text" v-model="form.premise_zipcode" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Mail Street</label>
      <div class="control">
        <input type="text" v-model="form.mail_street" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Mail City</label>
      <div class="control">
        <input type="text" v-model="form.mail_city" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Mail State</label>
      <div class="control">
        <input type="text" v-model="form.mail_state" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Mail Zipcode</label>
      <div class="control">
        <input type="text" v-model="form.mail_zipcode" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Manufacture</label>
      <div class="control">
        <input type="text" v-model="form.manufacture" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Model</label>
      <div class="control">
        <input type="text" v-model="form.model" class="input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Serial Number</label>
      <div class="control">
        <input type="text" v-model="form.serial_number" class="input" />
      </div>
    </div>
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
    <div class="field">
      <label class="label">Caliber/Gauge</label>
      <div class="control">
        <input type="text" v-model="form.caliber_gauge" class="input" />
      </div>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link" v-on:click="saveClick()">Submit</button>
      </div>
      <div class="control">
        <router-link class="button is-text" to="/acquisitions">
          Cancel
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "AcquisitonAddEdit",
  data() {
    return {
      types: {},
      data: [],
      seller_name: "",
      selected: null,
      isFetching: false,
      form: {
        id: '',
        seller: '',
        license_regn: '',
        license_dist: '',
        license_cnty: '',
        license_type: '',
        license_xprdte: '',
        license_seqn: '',
        license_name: '',
        business_name: '',
        premise_street: '',
        premise_city: '',
        premise_state: '',
        premise_zipcode: '',
        mail_street: '',
        mail_city: '',
        mail_state: '',
        mail_zipcode: '',
        manufacture: '',
        model: '',
        serial_number: '',
        type: '',
        caliber_gauge: ''
      }
    };
  },
  created: function(){
    var _this = this;

    // Load extra info from OPTIONS request.
    _this.$http({
      url: '/api/acquisitions/',
      method: 'OPTIONS',
    }).then(function(data) {
      _this.types = data.data.actions.POST.type.choices;
    });

    var acq_id = _this.$route.params.id;

    // Load acquisition.
    if (acq_id != undefined)
    {
        _this.$http({
          url: '/api/acquisitions/' + acq_id + '/',
          method: 'GET',
        }).then(function(data) {
          console.log(data);
          data = data.data;
          _this.form.id = data.id;
          _this.form.seller = data.seller;
          _this.form.license_regn = data.license_regn;
          _this.form.license_dist = data.license_dist;
          _this.form.license_cnty = data.license_cnty;
          _this.form.license_type = data.license_type;
          _this.form.license_xprdte = data.license_xprdte;
          _this.form.license_seqn = data.license_seqn;
          _this.form.license_name = data.license_name;
          _this.form.business_name = data.business_name;
          _this.form.premise_street = data.premise_street;
          _this.form.premise_city = data.premise_city;
          _this.form.premise_state = data.premise_state;
          _this.form.premise_zipcode = data.premise_zipcode;
          _this.form.mail_street = data.mail_street;
          _this.form.mail_city = data.mail_city;
          _this.form.mail_state = data.mail_state;
          _this.form.mail_zipcode = data.mail_zipcode;
          _this.form.manufacture = data.manufacture;
          _this.form.model = data.model;
          _this.form.serial_number = data.serial_number;
          _this.form.type = data.type;
          _this.form.caliber_gauge = data.caliber_gauge;
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
        .get(
          `api/dealers/?search=${
            this.seller_name
          }`
        )
        .then(({ data }) => {
          data.results.forEach(item => this.data.push(item));
          this.isFetching = false;
        })
        .catch(error => {
          this.isFetching = false;
          throw error;
        });
    },
    setSelectedSeller: function(option){
      this.selected = option;
      this.form.seller = option.seller;
      this.form.license_regn = option.license_regn;
      this.form.license_dist = option.license_dist;
      this.form.license_cnty = option.license_cnty;
      this.form.license_type = option.license_type;
      this.form.license_xprdte = option.license_xprdte;
      this.form.license_seqn = option.license_seqn;
      this.form.license_name = option.license_name;
      this.form.business_name = option.business_name;
      this.form.premise_street = option.premise_street;
      this.form.premise_city = option.premise_city;
      this.form.premise_state = option.premise_state;
      this.form.premise_zipcode = option.premise_zipcode;
      this.form.mail_street = option.mail_street;
      this.form.mail_city = option.mail_city;
      this.form.mail_state = option.mail_state;
      this.form.mail_zipcode = option.mail_zipcode;
      this.form.manufacture = option.manufacture;
      this.form.model = option.model;
      this.form.serial_number = option.serial_number;
      this.form.type = option.type;
      this.form.caliber_gauge = option.caliber_gauge;
    },
    saveClick: function(){
      var _this = this;
      //Save acquisition.
      var url;
      var item_id = this.$route.params.id
      var is_add = item_id === undefined;
      if (is_add){
          url = '/api/acquisitions/';
      } else {
          url = '/api/acquisitions/' + _this.form.id + '/';
      }
      this.$http({
          url: url,
          method: (is_add) ? 'POST' : 'PATCH',
          data: _this.form,
      }).then(function() {

        // Let the user know we saved the acquisition.
        _this.$snackbar.open({
          message: 'Saved!',
          type: 'is-success'
        });

        window.location.href = '#/acquisitions';
      });
    },
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
