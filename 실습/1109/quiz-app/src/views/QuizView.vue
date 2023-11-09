<template>
  <div>
    <div class="row justify-content-center mt-3">
      <QuizCreate class="col-8" 
      @create-quiz="updateQuiz" />
    </div>
    <div class="d-flex flex-column align-items-center justify-content-center mt-5">
      <div class="row justify-content-center">
        <div class="col-10" v-for="quiz in sortQuiz" :key="quiz.pk">
          <QuizDetail 
          :quiz="quiz" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import QuizDetail from '@/components/QuizDetail.vue';
  import QuizCreate from '@/components/QuizCreate.vue';
  import { computed, ref } from 'vue'
  
  const Quizs = ref([
    {pk: 1, question:'Python 웹 프레임워크 중 하나로, 마이크로 웹 프레임워크로 빠른 개발을 지원하는 것은?', answer: 'flask'},
    {pk: 2, question:'HTML에서 텍스트 입력란을 만드는 데 사용되는 요소는?', answer: 'input'},
    {pk: 3, question:'웹 어플리케이셔네서 클라이언트의 데이터를 서버로 전송할 때 주로 사용되는 HTTP 메서드는?', answer: 'post'},
    {pk: 4, question:'Python의 가상 환경을 만들어 프로젝트 별로 라이브러리 의존성을 격리시키는 명령어는?', answer: 'virtualenv'},
    {pk: 5, question:'웹 어플리케이션을 개발할 때, 사용자의 브라우저에 보여지는 부분을 렌더링하는 언어는 무엇인가요?', answer: 'html'},
  ])

  let newQuiz = {}
  const updateQuiz = function(newProblem){
    newQuiz = newProblem
    newQuiz.pk = Quizs.value.length + 1
    // console.log(newQuiz)
    Quizs.value.push(newQuiz)
  }
  const sortQuiz = computed(() => {
    return [...Quizs.value].sort((a, b) => b.pk - a.pk)
  })
  
</script>

<style scoped>

</style>