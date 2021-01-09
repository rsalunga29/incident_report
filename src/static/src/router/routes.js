import { AuthLayout, DashboardLayout } from '@/components/Layouts'

export const publicRoutes = [
  {
    path: '*',
    component: () => import(/* webpackChunkName: 'errors-404' */ '@/errors/NotFound.vue')
  },
  {
    path: '/auth',
    component: AuthLayout,
    meta: {
      title: 'Auth',
      group: 'auth'
    },
    children: [
      {
        path: 'login',
        name: 'Login',
        component: () => import(/* webpackChunkName: 'auth-login' */ '@/auth/Login.vue')
      },

      {
        path: 'register',
        name: 'Register',
        component: () => import(/* webpackChunkName: 'auth-register' */ '@/auth/Register.vue')
      },
    ],
  }
]

export const protectedRoutes = []
