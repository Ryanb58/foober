/* globals localStorage */

import axios from 'axios';
import * as Cookies from "js-cookie";


export default {
    login (email, pass, cb) {
      cb = arguments[arguments.length - 1]
      if (Cookies.get('jwttoken')) {
        if (cb) cb(true)
        this.onChange(true)
        return
      }
      loginRequest(email, pass, (res) => {
        if (res.authenticated) {
          Cookies.remove('jwttoken');
          Cookies.remove('jwttokenrefresh');
          Cookies.set('jwttoken', res.access);
          Cookies.set('jwttokenrefresh', res.refresh);
          if (cb) cb(true)
          this.onChange(true)
        } else {
          if (cb) cb(false)
          this.onChange(false)
        }
      })
    },

    getToken () {
      return Cookies.get('jwttoken');
    },

    logout (cb) {
      Cookies.remove('jwttoken');
      Cookies.remove('jwttokenrefresh');
      Cookies.remove('csrftoken');
      Cookies.remove('sessionid');
      if (cb) cb()
      this.onChange(false)
    },

    loggedIn () {
      return true;
      // return !!Cookies.get('jwttoken');
    },

    onChange () {},

    getAuthHeader () {
      if (Cookies.get('jwttoken')){
        return 'Bearer ' + Cookies.get('jwttoken');
      }
      return '';
    },
  }

  function loginRequest (email, pass, cb) {
    axios.post('/api/token/', {
        'username': email,
        'password': pass
    }).then(function(response){
      cb({
          authenticated: true,
          access: response.data.access,
          refresh: response.data.refresh,
      })
    })
    cb({ authenticated: false })
  }
