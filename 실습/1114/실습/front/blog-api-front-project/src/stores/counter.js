import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const posts = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getPosts = function(){
    axios({
      method: 'get',
      url: `${API_URL}/posts/posts/`,
    })
    .then((res) => {
      // console.log(res)
      posts.value = res.data
    })
    .catch((error) => {
      console.log(error)
    })
  }

  return { posts, API_URL, getPosts }
})
