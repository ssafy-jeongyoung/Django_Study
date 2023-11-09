<template>
  <div class="bg-light rounded border border-secondary-subtle p-3 m-3">
    <form action="">
      <h5 class="fw-bold">{{ quiz.pk }}번 문제. {{ quiz.question }}</h5>
      <p class="pt-2 mb-1">정답 입력</p>
      <input class="form-control" type="text" :id="quiz.pk">
    </form>
  </div>
</template>

<script setup>
  const props = defineProps(
    { quiz: Object },
  )
</script>

<style scoped>

</style>