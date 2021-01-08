import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

import router from './router'
import store from './store'

import App from './App.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(Vuex)
Vue.use(Buefy)

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
