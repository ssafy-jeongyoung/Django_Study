<template>
  <div class="border border-grey m-1 p-3">
    <h3 class="pb-2 mb-2">자식 페이지입니다.</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
    <p>용돈 : {{ child.balance }}</p>
    <button>용돈 주세요</button>
  </div>
</template>

<script setup>
  
  const props = defineProps({
    child: Object,
  })

  
</script>

<style scoped>

</style>