<template>
  <div>
    <div class="text-center p-3 mx-2 bg-light border border-secondary">
      <h3 class="pb-2">이름 : {{ card.name }}</h3>
      <p>직함 : {{ card.title }}</p>
      <button @click="deleteCardFunc">명함 삭제</button>
    </div>
  </div>
</template>

<script setup>
  const emit = defineEmits(['deleteCardEvent'])

  const props = defineProps({
    card: Object,
  })

  const deleteCardFunc = function() {
    emit('deleteCardEvent', props.card)
  }
</script>

<style scoped>

</style>