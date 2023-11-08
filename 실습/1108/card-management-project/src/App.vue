<script setup>
  import BusinessCard from '@/components/BusinessCard.vue';
  import CreateCardForm from '@/components/CreateCardForm.vue';
</script>

<template>
  <header class="d-flex flex-row justify-content-center">
    <h1 class="m-3 p-5 bg-info bg-gradient text-white">명함 관리 페이지</h1>
  </header>
  <main class="d-flex flex-row justify-content-center mt-3">
    <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
  </main>
  <article>
    <CreateCardForm />
    <BusinessCard />
  </article>
  <footer class="fixed-bottom text-center bg-secondary bg-gradient pt-3 pb-2">
    ⓒ2023 My Business Cards
  </footer>
</template>

<style scoped>

</style>
