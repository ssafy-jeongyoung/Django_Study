<template>
    <div>
        <div v-if="videoSelected">
            <iframe :src="videoUrl" frameborder="0"></iframe>
            <p>title : {{ videoSelected?.snippet.title }}</p>
        </div>
        <p v-else>선택된 비디오가 없습니다.</p>
    </div>
</template>

<script setup>
import { computed } from '@vue/reactivity';

    const props = defineProps({
        videoSelected : Object,
    })

    const videoUrl = computed(() => {
        return `https://www.youtube.com/embed/${props.videoSelected?.id.videoId}`
    })
</script>
    
<style scoped>

</style>