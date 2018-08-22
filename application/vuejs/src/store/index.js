import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from 'vuex/dist/logger';
import home from './pages/home';

Vue.use(Vuex);

export default new Vuex.Store({
  strict: true,
  plugins: process.env.NODE_ENV !== 'production'
    ? [createLogger()]
    : []
  ,
  modules: {
    home,
  },
})
