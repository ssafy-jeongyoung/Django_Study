<template>
  <div class="bg-light rounded border border-secondary-subtle p-3 m-3">
    <form action="" @submit="submitAns">
      <h5 class="fw-bold">{{ quiz.pk }}번 문제. {{ quiz.question }}</h5>
      <p class="pt-2 mb-1">정답 입력</p>
      <input class="form-control" v-model="inputAns" type="text" :id="quiz.pk">
    </form>
  </div>
</template>

<script setup>
  import { useRoute, useRouter } from 'vue-router';
  import { ref } from 'vue'
  import router from '../router';

  const route = useRoute()
  const inputAns = ref('')
  const props = defineProps(
    { quiz: Object },
  )
  const pk = props.quiz.pk
  const answer = props.quiz.answer

  const submitAns = function(){
    router.push({name:'answer', params:{pk:pk, answer:answer}, query:{myAns:inputAns.value}})
  }
</script>

<style scoped>

</style>