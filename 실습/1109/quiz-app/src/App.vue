<script setup>

</script>

<template>
  <header class="container text-center">
    <div class="row justify-content-center">
      <div class="col-8 grey pb-2">
        <div>
          <p class="fs-3 fw-bold text-white rounded-top bg-warning p-3 mt-2 mb-0">Quiz 퀴즈</p>
          <p class="bg-white rounded-bottom p-4">여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
        </div>
        <nav class="container align-middle bg-black p-1">
          <RouterLink :to="{ name:'home' }" class="text-white text-decoration-none px-3 border-end border-white border-2">Home</RouterLink>
          <RouterLink :to="{ name:'quiz' }" class="text-white text-decoration-none px-3 border-end border-white border-2">Quiz</RouterLink>
        </nav>
      </div>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
  .grey {
    background-color: #dee2e6;
  }
</style>
