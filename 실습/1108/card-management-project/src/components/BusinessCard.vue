<template>
  <div>
    <h2 class="col-12 text-center pt-5">보유 명함 목록</h2>
    <div v-if="businessCards.length > 0" class="row justify-content-center">
      <p class="col-12 text-center pt-2">현재 보유 중인 명함 수 : {{ businessCards.length }}</p>
      <businessCardDetail 
      class="col-5 p-3"
      v-for="card of businessCards"
      :key="card.name"
      :card="card"
      @delete-card-event="deleteCard" />
    </div>
    <p v-else class="text-center">명함이 없습니다. 새로운 명함을 추가해 주세요</p>
  </div>
</template>

<script setup>
  import businessCardDetail from '@/components/businessCardDetail.vue';
  import { ref } from 'vue'

  defineProps({businessCards: Array})

  const businessCards = ref([
    {name:'일론 머스크', title:'테슬라 테크노킹'},
    {name:'래리 엘리슨', title:'오라클 창업주'},
    {name:'빌 게이츠', title:'마이크로소프트 공동창업주'},
    {name:'래리 페이지', title:'구글 공동창업주'},
    {name:'세르게이 브린', title:'구글 공동창업주'},
  ])

  const deleteCard = function(card) {
    const index = businessCards.value.findIndex(item => item.name === card.name)
    if (businessCards !== -1) {
      businessCards.value.splice(index, 1); // 해당 인덱스의 요소를 삭제
    }
  }
</script>

<style scoped>

</style>