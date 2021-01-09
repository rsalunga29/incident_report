import store from '@/store'

function login(to, from, next) {
  let token = localStorage.getItem('token')

  if (token) {
    store.commit('auth/SET_USER_LOGIN', token)
    next()
  } else {
    if (to.path !== '/auth/login' && to.path !== '/auth/register') {
      next('/auth/login')
    } else {
      next()
    }
  }
}

function logout(next) {
  next()
}

export default {
  login,
  logout
}
