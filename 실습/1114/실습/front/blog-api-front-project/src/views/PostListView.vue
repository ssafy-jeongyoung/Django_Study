<template>
  <div class="container">
    <h1>게시글 목록 페이지</h1>
    <hr>
    <PostListItem 
    v-for="post in store.posts" 
    :key="post.pk" 
    :post="post" />
  </div>
</template>

<script setup>
  import PostListItem from '@/components/PostListItem.vue';
  import { onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter';
  import { RouterLink } from 'vue-router'

  const store = useCounterStore()

  onMounted(() => {
    store.getPosts()
  })
</script>

<style scoped>

</style>