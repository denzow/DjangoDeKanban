import Vue from 'vue';
import router from './router/index';
import store from './store/index';

Vue.config.productionTip = false;

/* eslint-disable */
new Vue({
  router,
  store,
  el: '#app',
});
