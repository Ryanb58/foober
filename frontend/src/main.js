import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';
import Buefy from 'buefy';
import 'buefy/lib/buefy.css';
import moment from 'moment';
// import vuemoment from 'vue-moment';

import router from './router';
// import auth from './utils/auth';

axios.defaults.baseURL = 'http://localhost:8000/';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';


Vue.use(axios);
Vue.use(Buefy);
Vue.use(moment);
// Vue.use(vuemoment);

Vue.prototype.$http = axios;
Vue.prototype.$moment = moment;

// Vue.prototype.$http.interceptors.request.use(function(config) {
//   const token = auth.getToken();

//   if ( token != null ) {
//     config.headers.Authorization = `Bearer ${token}`;
//   }

//   return config;
// }, function(err) {
//   return Promise.reject(err);
// });

// // Add a 401 response interceptor
// Vue.prototype.$http.interceptors.response.use(function (response) {
//   return response;
// }, function (error) {
//   if (error.hasOwnProperty('response') && 401 === error.response.status) {
//     window.location = '#/login';
//   }
//   return Promise.reject(error);
// });

Vue.config.productionTip = false;



new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
