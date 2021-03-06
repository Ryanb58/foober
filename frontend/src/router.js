import Vue from 'vue';
import Router from 'vue-router';
import Index from './components/Index.vue';

import Login from '@/components/Login.vue';
import FoodList from '@/components/FoodList.vue';
import FoodAddEdit from '@/components/FoodAddEdit.vue';
import Resources from '@/components/Resources.vue';
import Map from '@/components/Map.vue';

import auth from '@/utils/auth';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index,
      // beforeEnter: requireAuth,
    },
    {
      path: '/resources',
      name: 'resources',
      component: Resources,
      // beforeEnter: requireAuth,
    },
    {
      path: '/map',
      name: 'map',
      component: Map,
      // beforeEnter: requireAuth,
    },
    {
      path: '/food',
      name: 'food-list',
      component: FoodList,
      // beforeEnter: requireAuth,
    },
    {
      path: '/food/addedit/',
      name: 'food-addedit',
      component: FoodAddEdit,
      // beforeEnter: requireAuth,
    },
    {
      path: '/food/addedit/:id',
      name: 'food-addedit-id',
      component: FoodAddEdit,
      // beforeEnter: requireAuth,
    },
    // {
    //   path: '/dispositions/addedit/:id',
    //   name: 'dispositions-addedit-id',
    //   component: DispositionAddEdit,
    //   beforeEnter: requireAuth,
    // },
    // { path: '/login', component: Login },
    // { path: '/logout',
    //   beforeEnter (to, from, next) {
    //     auth.logout()
    //     next('/')
    //   }
    // }
  ]
})


// function requireAuth (to, from, next) {
//   if (!auth.loggedIn()) {
//     next({
//       path: '/login',
//       query: { redirect: to.fullPath }
//     })
//   } else {
//     next()
//   }
// }
