<template>
    <div class="card">
        <h1>가수 이름</h1>
        <img src="../../assets/singer.jpg" alt="singer">
        <p>가수 소개글</p>
        <SingerAlbum />
        <SingerAlbum />
    </div>
</template>

<script setup>
    import SingerAlbum from '@/components/singers/SingerAlbum.vue';
</script>

<style scoped>
    img {
        width: 200px;
        border-radius: 70%;
        object-fit: cover;
    }
    .card {
        border: 1px solid black;
        display: inline-block;
        width: 40%;
        margin: 20px;
    }
</style>