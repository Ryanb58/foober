<template>
  <section>
    <div>
      <div class="control">
        <router-link tag='button' class='button is-primary' to='/food/addedit'>Add Food</router-link>
      </div>
    </div>
    <b-table
      :data="data"
      :loading="loading"

      paginated
      backend-pagination
      :total="total"
      :per-page="perPage"
      @page-change="onPageChange"

      backend-sorting
      :default-sort-direction="defaultSortOrder"
      :default-sort="[sortField, sortOrder]"
      @sort="onSort">

      <template slot-scope="props">
        <b-table-column field="name" label="Food" width="500">
          {{ props.row.name | truncate(120) }}
        </b-table-column>

        <b-table-column field="contact_name" label="Contact" numeric sortable>
          {{ props.row.contact_name }}
        </b-table-column>

        <b-table-column field="available_timestamp" label="Available" sortable>
          {{ props.row.available_timestamp ? new Date(props.row.available_timestamp).toLocaleDateString() : '' }}
        </b-table-column>

        <b-table-column label="">
          <div class="control">
            <router-link class="button is-light" :to="{ name: 'food-addedit-id', params: { id: props.row.id }}">
              Edit
            </router-link>
          </div>
        </b-table-column>

      </template>
    </b-table>
  </section>
</template>

<script>
export default {
  data() {
    return {
      data: [],
      total: 0,
      loading: false,
      sortField: "name",
      sortOrder: "desc",
      defaultSortOrder: "desc",
      page: 1,
      perPage: 20
    };
  },
  methods: {
    /*
            * Load async data
            */
    loadAsyncData() {
      var _this = this;

      var sortField = this.sortField;
      if (this.sortOrder == "desc") {
        sortField = "-" + sortField;
      }
      const params = [`ordering=${sortField}`, `page=${this.page}`].join("&");

      this.loading = true;
      var url = "/api/food/v1/item/?" + params;
      this.$http
        .get(url)
        .then(({ data }) => {
          _this.apiCurrentUrl = url;
          _this.data = data.results;
          _this.apiNextUrl = data.next;
          _this.apiPreviousUrl = data.previous;
          _this.total = data.count;
          _this.perPage = data.results.length;
          _this.loading = false;
        })
        .catch(error => {
          _this.data = [];
          _this.total = 0;
          _this.loading = false;
          throw error;
        });
    },
    /*
            * Handle page-change event
            */
    onPageChange(page) {
      this.page = page;
      this.loadAsyncData();
    },
    /*
            * Handle sort event
            */
    onSort(field, order) {
      this.sortField = field;
      this.sortOrder = order;
      this.loadAsyncData();
    },
    /*
            * Type style in relation to the value
            */
    type(value) {
      const number = parseFloat(value);
      if (number < 6) {
        return "is-danger";
      } else if (number >= 6 && number < 8) {
        return "is-warning";
      } else if (number >= 8) {
        return "is-success";
      }
    },
  },
  filters: {
    /**
     * Filter to truncate string, accepts a length parameter
     */
    truncate(value, length) {
      return value.length > length ? value.substr(0, length) + "..." : value;
    }
  },
  mounted() {
    this.loadAsyncData();
  }
};
</script>