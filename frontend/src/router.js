import Vue from 'vue';
import Router from 'vue-router';
import Index from './components/Index.vue';
// import AcquisitionList from './components/AcquisitionList.vue';
// import Dashboard from './components/Dashboard.vue';
// import DispositionAddEdit from './components/DispositionAddEdit.vue';

// import Login from '@/components/Login.vue';

// import auth from '@/utils/auth';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index,
    //   beforeEnter: requireAuth,
    }
    // {
    //   path: '/acquisitions',
    //   name: 'acquisition-list',
    //   component: AcquisitionList,
    //   beforeEnter: requireAuth,
    // },
    // {
    //   path: '/acquisitions/addedit/',
    //   name: 'acquisitions-addedit',
    //   component: AcquisitionAddEdit,
    //   beforeEnter: requireAuth,
    // },
    // {
    //   path: '/acquisitions/addedit/:id',
    //   name: 'acquisitions-addedit-id',
    //   component: AcquisitionAddEdit,
    //   beforeEnter: requireAuth,
    // },
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
