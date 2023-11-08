<template>
    <div>
        <ul>
            <VideoListItemComponent 
            v-for="video of videoList"
            :key="video.id.videoId"
            :video="video"
            @item-select="onItemSelect" />
        </ul>
    </div>
</template>

<script setup>
    import VideoListItemComponent from '@/components/VideoListItemComponent.vue';

    defineProps(
        { videoList: Array },
    )

    const emit = defineEmits(['itemSelect'])

    const onItemSelect = function(video){
        emit('itemSelect', video)
    }
</script>

<style scoped>

</style>