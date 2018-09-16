import Vue from 'vue';
import store from '@/store';
import VueNativeSock from 'vue-native-websocket';


export default function WebSocketMiddleware(router) {
  // ダイナミックにwsをつなげる
  router.beforeEach((to, from, next) => {
    if (from.meta.ws) {
      Vue.prototype.$disconnect();
      // Remove plugin instance
      const index = Vue._installedPlugins.indexOf(VueNativeSock);
      if (index > -1) {
        Vue._installedPlugins.splice(index, 1);
      }
    }

    if (to.meta.ws) {
      console.log(to, `/ws${to.path}`);
      Vue.use(VueNativeSock, `//${window.location.host}/ws${to.meta.ws(to)}`, {
        connectManually: true,
        reconnection: true,
        reconnectionAttempts: 5,
        reconnectionDelay: 3000,
        format: 'json',
        store,
      });
      Vue.prototype.$connect();
    }
    next();
  });
}
