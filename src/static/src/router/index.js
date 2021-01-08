import Vue from 'vue'
import Router from 'vue-router'
import { publicRoutes, protectedRoutes } from './routes'

Vue.use(Router)

const routes = publicRoutes.concat(protectedRoutes)

const router = new Router({
  mode: 'history',
  linkActiveClass: 'active',
  routes: routes
})

export default router
