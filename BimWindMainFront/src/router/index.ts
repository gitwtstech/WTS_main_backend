import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/registration',
      name: 'registration',
      component: () => import('../components/Submit.vue')
    },
    {
      path: '/components',
      name: 'components',
      component: () => import('../components/ModelComponents.vue')
    },
    {
      path: '/plugins',
      name: 'plugins',
      component: () => import('../components/Plugins.vue')
    }
  ]
})

export default router
