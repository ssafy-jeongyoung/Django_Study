<template>
  <div>
    <h4>{{ post.pk }}번 POST</h4>
    <p>제목 : {{ post.title }}</p>
    <p>내용 : {{ post.content }}</p>
    <hr>
  </div>
</template>

<script setup>
  defineProps({
    post : Object,
  })
</script>

<style scoped>

</style>