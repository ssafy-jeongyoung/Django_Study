<template>
  <div class="row justify-content-center border">
    <h5 class="text-center">{{ product.name }}</h5>
    <img :src="product.imagePath" alt="">
    <p class="text-center">{{ product.price }}</p>
    <p class="text-center" v-if="!product.isFavorite">🤍</p>
    <p class="text-center" v-else>❤️</p>
  </div>
</template>

<script setup>
  const props = defineProps({product:Object})

  const product = props.product
</script>

<style scoped>
  img {
    width: 500px;
    height: 300px;
  }
</style>