const state = {
  status: { loggedIn: false }
}

const getters = {}

const mutations = {}

const actions = {
  login({ commit }, data) {
    console.log(data)
  },

  register({ dispatch, commit }, data) {
    console.log(data)
  }
}

export default {
  namespace: true,
  state,
  getters,
  mutations,
  actions,
}
