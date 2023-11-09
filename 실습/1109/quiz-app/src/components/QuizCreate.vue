<template>
  <div class="row justify-content-center">
    <div class="col-12 grey pb-2 rounded">
      <form @submit.prevent="createQuiz">
        <p class="pt-5 pb-2 fw-bold fs-4">퀴즈 생성</p>
        <p class="mb-0">문제</p>
        <textarea class="form-control" name="problem" id="" rows="5" v-model="problem"></textarea>
        <p class="mb-0">답안</p>
        <input class="form-control" type="text" v-model="answer">
        <p class="mt-3"><button class="form-control btn btn-primary">퀴즈 생성</button></p>
      </form>
      </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const problem = ref('')
  const answer = ref('')

  const emit = defineEmits(['createQuiz'])

  const createQuiz = function () {
    const newProblem = { question:problem.value, answer:answer.value }
    emit('createQuiz', newProblem)
    problem.value = ''
    answer.value = ''
  }
</script>

<style scoped>
  .grey {
    background-color: #dee2e6;
  }

</style>