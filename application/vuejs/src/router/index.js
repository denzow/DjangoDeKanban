import Vue from 'vue';
import Router from 'vue-router';
import DefaultLayout from '../components/layouts/DefaultLayout.vue';
import NotFound from '../pages/NotFound.vue';
import Home from '../pages/Home.vue';


Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: DefaultLayout,
      children: [
        {
          path: '',
          component: Home,
        }
      ]
    },
    {
      path: '*',
      component: NotFound,
    }
  ]
})
