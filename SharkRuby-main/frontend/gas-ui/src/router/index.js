import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ResultsView from '../views/ResultsView.vue'
import StarsView from '../views/StarsView.vue'
import SearchView from '../views/SearchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
        path: '/search/query/:query',
        name: 'query',
        component: ResultsView,
        props: true
    },
    {
        path: '/search/gps/:lat/:long',
        name: 'gps',
        component: ResultsView,
        props: true
    },
    {
        path: '/stars',
        name: 'stars',
        component: StarsView
    },
    {
        path: '/search',
        name: 'search',
        component: SearchView
    }
  ]
})

export default router
