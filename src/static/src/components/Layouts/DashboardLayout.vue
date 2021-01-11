<template>
  <section>
    <b-navbar
      wrapper-class="container"
      class="is-success"
    >
      <template #start>
        <router-link
          class="navbar-item"
          :to="{ path: '/' }"
        >Issues</router-link>

        <router-link
          class="navbar-item"
          :to="{ path: '/dashboard/tasks' }"
        >My Tasks</router-link>
      </template>

      <template #end>
        <b-navbar-dropdown :label="userInfo().name">
          <b-navbar-item @click="logout">
            Logout
          </b-navbar-item>
        </b-navbar-dropdown>
      </template>
    </b-navbar>

    <div class="container pt-6">
      <router-view :key="$route.path" />
    </div>
  </section>
</template>

<script>
import { mapState } from 'vuex';

export default {
  methods: {
    logout() {
      this.$store.dispatch('auth/logout').then((response) => {
        this.$router.push({ path: '/auth/login' });
      });
    },

    ...mapState('auth', ['userInfo']),
  },
};
</script>

<style scoped>
.navbar-item > a {
  color: #fff;
}
</style>
