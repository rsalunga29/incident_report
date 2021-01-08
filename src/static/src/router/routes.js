export const publicRoutes = [
  {
    path: '/auth',
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
        component: () => import(/* webpackChunkName: 'auth-login' */ '@/auth/Register.vue')
      },
    ],
  }
]

export const protectedRoutes = []
