import { AuthLayout, DashboardLayout } from '@/components/Layouts'

export const publicRoutes = [
  {
    path: '*',
    component: () => import(/* webpackChunkName: 'errors-404' */ '@/errors/NotFound.vue')
  },

  { // @TODO: Disable route if user is already logged in
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

export const protectedRoutes = [
  {
    path: '/',
    redirect: '/dashboard',
  },

  {
    path: '/dashboard',
    component: DashboardLayout,
    redirect: '/dashboard/issues',
    meta: {
      title: 'Dashboard',
      group: 'dashboard',
    },
    children: [
      {
        path: 'issues',
        name: 'issues-dashboard',
        component: () => import(/* webpackChunkName: 'issues-overview' */ '@/issues/Overview.vue'),
      },

      {
        path: 'tasks',
        name: 'tasks-dashboard',
        component: () => import(/* webpackChunkName: 'tasks-overview' */ '@/tasks/Overview.vue'),
      }
    ],
  }
]
