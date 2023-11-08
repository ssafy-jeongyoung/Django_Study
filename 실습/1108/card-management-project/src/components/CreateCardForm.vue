<template>
  <div>
    <form class="d-flex justify-content-center align-items-center" @submit.prevent="createCardFunc">
      <label class="pe-2" for="name">이름  </label>
      <input class="pe-5 me-4 border border-info rounded" type="text" id="name">
      <label class="pe-2" for="title">직함  </label>
      <input class="pe-5 border border-info rounded" type="text" id="title">
      <button type="submit" class="btn btn-outline-primary ms-3">명함 추가</button>
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  const emit = defineEmits(['createCardFunc'])

  const createCardFunc = function() {
    const cardInfo = {}

  }
</script>

<style scoped>

</style>