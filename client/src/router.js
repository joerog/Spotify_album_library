import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping.vue';
import Albums from './components/Albums.vue';
import Callback from './components/Callback.vue';
import Top from './components/Top.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/albums',
      name: 'Albums',
      component: Albums,
    },
    {
      path: '/callback',
      name: 'Callback',
      component: Callback,
    },
    {
      path: '/top',
      name: 'Top',
      component: Top,
    },
  ],
});
