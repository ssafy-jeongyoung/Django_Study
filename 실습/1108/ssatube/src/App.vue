<script setup>
  import SearchBar from '@/components/SearchBar.vue';
  import VideoDetail from '@/components/VideoDetail.vue';
  import VideoListComponent from '@/components/VideoListComponent.vue';

  import { onMounted, ref } from 'vue'
  import axios from 'axios'

  const API_URL = 'https://www.googleapis.com/youtube/v3/search'
  const videoList = ref([])
  const selectedVideo = ref(null)
  const keyword = ref('')

  const onItemSelect = function(video) {
    selectedVideo.value = video
  }

  onMounted(() => {
    axios({
      url: API_URL,
      params:{
        type : 'video',
        part : 'snippet',
        key : 'AIzaSyCmKh1n9XfYAJm7faoZg7KBpkjmlUWCxgQ',
        q : 'ssafy'
      }
    })
    .then((response) => {
      // console.log(response.data)
      videoList.value = response.data.items
    })
  })

</script>

<template>
  <header class="container">
    <SearchBar />
  </header>
  <main class="container">
    <div class="d-flex flex-row justify-content-between">
      <div>
        <VideoDetail 
        :video-selected="selectedVideo" />
      </div>
      <div>
        <VideoListComponent  
        :video-list="videoList" 
        @item-select="onItemSelect"
        />
      </div>
    </div>
  </main>
</template>

<style scoped>

</style>
