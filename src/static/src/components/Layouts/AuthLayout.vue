<template>
  <section>
    <div
      class="hero is-success"
      style="height: 10rem;"
    ></div>

    <router-view :key="$route.path" />
  </section>
</template>

<script>
export default {
  //
};
</script>
