<template>
    <li @click="onClick">
        <img :src="video.snippet.thumbnails.default.url" alt="">
        <!-- <p>id : {{ video.id }}</p> -->
        <p>{{ video.snippet.title }}</p>
    </li>
</template>

<script setup>
    const emit = defineEmits(['itemSelect'])

    const props = defineProps({
        video: Object,
    })

    const onClick = function() {
        emit('itemSelect', props.video)
    }
</script>

<style scoped>

</style>