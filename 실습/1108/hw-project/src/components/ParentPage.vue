<template>
  <div class="border border-grey m-2 p-3">
    <h1>부모 페이지입니다.</h1>
    <ChildPage 
    v-for="child of children"
    :key="child.name"
    :child="child" />
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import ChildPage from '@/components/ChildPage.vue';
  const children = ref([
    {name:'김하나', age:30, balance:100000},
    {name:'김두리', age:20, balance:10000},
    {name:'김서이', age:10, balance:1000},  
  ])

  const props = defineProps({
    child: Object,
  })
</script>

<style scoped>

</style>