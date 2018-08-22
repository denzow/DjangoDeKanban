import Vue from 'vue';
import router from './router/index';
import store from './store/index';

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  el: '#app'
});