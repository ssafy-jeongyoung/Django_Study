<script setup>
  import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
    <nav class="p-4 m-3 text-center bg-black">
      <RouterLink :to="{name:'main'}" class="fw-bold fs-4 text-decoration-none text-white mx-3">Home</RouterLink>
      <RouterLink :to="{name:'posts'}" class="fw-bold fs-4 text-decoration-none text-white mx-3">PostList</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
