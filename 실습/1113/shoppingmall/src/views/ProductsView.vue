<template>
  <div class="p-3 m-2">
    <h3 class="mx-3 fw-bold">상품 목록 페이지</h3>
    <div class="row">
      <ProductDetail v-for="product in products"
      :key="product.name"
      :product="product"
      class="col-4 m-0" />
    </div>
  </div>
</template>

<script setup>
  import ProductDetail from '@/components/ProductDetail.vue';
  import {useCounterStore} from '@/stores/products'

  const store = useCounterStore()

  const products = store.productList
</script>

<style scoped>

</style>