import Vue from 'vue'
import VueRouter from 'vue-router'

import { publicRoutes, protectedRoutes } from './routes'
import store from '@/store'
import basicAuthProvider from '@/auth/basicAuthProvider'

Vue.use(VueRouter)

const routes = publicRoutes.concat(protectedRoutes)

const router = new VueRouter({
  mode: 'history',
  linkActiveClass: 'active',
  routes: routes
})

router.beforeEach((to, from, next) => {
  if (!store.state.auth.status.loggedIn) {
    basicAuthProvider.login(to, from, next)
  } else {
    if (!store.state.auth.userInfo) {
      // getUserInfo
    }
  }
  next()
})

export default router
