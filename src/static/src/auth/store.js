import jwt_decode from 'jwt-decode'
import { SnackbarProgrammatic as Snackbar } from 'buefy'
import { debounce } from 'lodash'
import router from '@/router'
import UserAPI from './api'

const state = {
  status: { loggedIn: false },
  accessToken: localStorage.getItem('token') || null,
  userInfo: { name: '', email: '' },
  usersList: [],
}

const getters = {
  accessToken: () => state.accessToken,
  email: () => state.userInfo.email,
  name: () => state.userInfo.name,
  usersList: () => state.usersList
}

const mutations = {
  SET_USER_LOGIN(state, accessToken) {
    state.accessToken = accessToken
    state.status.loggedIn = true
    state.userInfo = jwt_decode(accessToken)

    localStorage.setItem('token', accessToken)
  },

  SET_USER_LOGOUT(state) {
    state.accessToken = null
    state.status.loggedIn = false
    state.userInfo = null

    localStorage.removeItem('token')
  },

  SET_ALL_USERS(state, value) {
    state.usersList = value
  }
}

const actions = {
  login({ commit }, data) {
    UserAPI.login(data.email, data.password)
      .then(response => {
        commit('SET_USER_LOGIN', response.data.token)
        router.push({ path: '/' })
      })
      .catch(error => {
        Snackbar.open({
          type: 'is-danger',
          message: error.response.data.detail,
          position: 'is-bottom-right',
        })
      })
  },

  register({ dispatch, commit }, data) {
    UserAPI.register(data.name, data.email, data.password)
      .then(response => {
        dispatch('login', data)
      })
      .catch(error => {
        console.log(error)
        Snackbar.open({
          type: 'is-danger',
          message: `Cannot create user. Reason: ${error.response.data.detail}`,
          position: 'is-bottom-right',
        })
      })
  },

  logout({ commit }) {
    commit('SET_USER_LOGOUT')
  },

  getAllUsers: debounce(({ commit }) => {
    return UserAPI.getAll().then(response => {
      commit('SET_ALL_USERS', response.data)
    })
  }, 2000),
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}
