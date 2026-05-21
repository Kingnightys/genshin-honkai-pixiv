<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Video {
  id: number
  title: string
  thumbnail: string
  duration: string
}

const videos = ref<Video[]>([])
const isLoading = ref(true)

// Mock数据
const mockVideos: Video[] = [
  { id: 1, title: '原神4.0 PV', thumbnail: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20fontaine%20pv%20thumbnail&width=320&height=180', duration: '3:45' },
  { id: 2, title: '星穹铁道PV', thumbnail: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20pv%20thumbnail&width=320&height=180', duration: '2:30' },
]

const fetchVideos = async () => {
  try {
    const response = await axios.get('http://192.168.8.49:8000/api/videos')
    videos.value = response.data.data || mockVideos
  } catch {
    videos.value = mockVideos
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchVideos()
})
</script>

<template>
  <section id="pv" class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-4xl font-bold text-center mb-12">PV展览</h2>

      <div v-if="isLoading" class="flex justify-center">
        <div class="w-10 h-10 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div 
          v-for="video in videos" 
          :key="video.id"
          class="bg-slate-800/50 rounded-xl overflow-hidden border border-slate-700 hover:border-purple-500/50 transition-all cursor-pointer group"
        >
          <div class="relative">
            <img :src="video.thumbnail" :alt="video.title" class="w-full h-48 object-cover" />
            <div class="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
              <i class="fa fa-play text-white text-4xl"></i>
            </div>
            <span class="absolute bottom-2 right-2 bg-black/70 px-2 py-1 rounded text-sm">{{ video.duration }}</span>
          </div>
          <div class="p-4">
            <h3 class="font-bold">{{ video.title }}</h3>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
