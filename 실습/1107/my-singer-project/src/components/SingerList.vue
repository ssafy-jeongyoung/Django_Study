<template>
    <div>
        <h1>가수 정보 페이지에 오신 것을 환영합니다.</h1>
        <p>여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요.</p>
        <img src="../assets/microphone.jpg" alt="mic">
        <h1 class="h1_orange">가수 목록</h1>
        <SingerDetail v-for="singer in singers"/>

    </div>
</template>

<script setup>
    import SingerDetail from '@/components/singers/SingerDetail.vue';
    import { ref } from 'vue'

    const singers = ref([
        { name:'adele'},
        { name:'maroon 5'},
        { name:'Dua Lipa'},
    ])
</script>

<style scoped>
    div {
        text-align: center;
    }

    img {
        width: 200px;
    }
    .h1_orange {
        color: orangered;
    }
</style>
