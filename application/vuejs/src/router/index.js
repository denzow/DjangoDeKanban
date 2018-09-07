import Vue from 'vue';
import Router from 'vue-router';
import WebSocketMiddleware from './middlewares/websocket';

import DefaultLayout from '../components/layouts/DefaultLayout.vue';
import NotFound from '../pages/NotFound.vue';
import Home from '../pages/Home/Index.vue';
import Board from '../pages/Board/Index.vue';
import CardShow from '../pages/Board/Card/Show.vue';


Vue.use(Router);

const router = new Router({
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
        },
        {
          path: 'board/:boardId',
          component: Board,
          props: route => ({ boardId: parseInt(route.params.boardId, 10) }),
          meta: {
            ws: route => route.path,
          },
          children: [
            {
              path: 'card/:cardId',
              component: CardShow,
              props: route => ({
                cardId: parseInt(route.params.cardId, 10),
                boardId: parseInt(route.params.boardId, 10),
              }),
              meta: {
                ws: route => route.path.split('/card')[0],
              },
            },
          ],
        },
      ],
    },
    {
      path: '*',
      component: NotFound,
    },
  ],
});

WebSocketMiddleware(router);
export default router;
