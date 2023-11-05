import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/courses',
      name: 'courses',
      component: () => import('../views/CoursesView.vue')
    },
    {
      path: '/plugins',
      name: 'plugins',
      component: () => import('../views/PluginsView.vue')
    },
    {
      path: '/components',
      name: 'components',
      component: () => import('../views/ComponentsLibView.vue')
    },
    {
      path: '/auth/login',
      name: 'auth/login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/auth/register',
      name: 'auth/register',
      component: () => import('../views/RegisterView.vue')
    }
  ]
})

export default router
