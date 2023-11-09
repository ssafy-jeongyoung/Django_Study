<template>
  <div class="row justify-content-center mt-4">
    <div class="col-8 grey pb-2 rounded">
      <p class="text-center pt-3 mb-0">{{ pk }}번 문제</p>
      <p class="text-center fw-bold fs-4 pb-2">정답 확인</p>
      <div class="row justify-content-center mt-4">
        <div v-if="myAns===answer" class="col-11 pb-2 rounded bg-white mb-2">
          <p class="fw-bold fs-5 mt-4 text-success">정답입니다!</p>
          <p class="text-success">나의 제출 답안 : {{ myAns }}</p>
          <p>정답 : {{ answer }}</p>
        </div>
        <div v-else class="col-11 pb-2 rounded bg-white mb-2">
          <p class="fw-bold fs-5 mt-4 text-danger">오답입니다!</p>
          <p class="text-danger">나의 제출 답안 : {{ myAns }}</p>
          <p>정답 : {{ answer }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
import { useRoute } from 'vue-router';

  const route = useRoute()
  const pk = ref(route.params.pk)
  const answer = ref(route.params.answer)
  const myAns = ref(route.query.myAns)


</script>

<style scoped>
.grey {
    background-color: #dee2e6;
  }
</style>