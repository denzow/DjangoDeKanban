import Vue from 'vue';
import Vuex from 'vuex';
import createLogger from 'vuex/dist/logger';
import home from './pages/home';
import board from './pages/board';


Vue.use(Vuex);

export default new Vuex.Store({
  strict: true,
  plugins: process.env.NODE_ENV !== 'production'
    ? [createLogger()]
    : [],
  modules: {
    home,
    board,
  },
  state: {
    socket: null,
  },
  mutations: {
    SOCKET_ONOPEN(state, event) {
      console.log('SOCKET_ONOPEN', event);
      // 接続時にStoreにwebsocketオブジェクトを登録する
      state.socket = event.target;
    },
    SOCKET_ONCLOSE(state, event) {
      console.log('SOCKET_ONCLOSE', event);
      // 接続終了にStoreにwebsocketオブジェクトを解除する
      state.socket = null;
    },
    SOCKET_ONERROR(state, event) {
      console.log('SOCKET_ONERROR', event);
    },
    // default handler called for all methods
    SOCKET_ONMESSAGE(state, message) {
      console.log('SOCKET_ONMESSAGE', message);
    },
    // mutations for reconnect methods
    SOCKET_RECONNECT(state, count) {
      console.log('SOCKET_RECONNECT', count);
    },
    SOCKET_RECONNECT_ERROR(state) {
      console.log('SOCKET_RECONNECT_ERROR', state);
    },
  },
});

