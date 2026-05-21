<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Music {
  id: number
  title: string
  artist: string
  cover_url: string
  duration: string
}

const music = ref<Music[]>([])
const isLoading = ref(true)

// Mock数据
const mockMusic: Music[] = [
  { id: 1, title: '璃月', artist: 'HOYO-MiX', cover_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=liyue%20ost%20cover&width=150&height=150', duration: '4:32' },
  { id: 2, title: '稻妻', artist: 'HOYO-MiX', cover_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=inazuma%20ost%20cover&width=150&height=150', duration: '5:18' },
  { id: 3, title: '星穹铁道', artist: 'HOYO-MiX', cover_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20ost%20cover&width=150&height=150', duration: '3:45' },
]

const fetchMusic = async () => {
  try {
    const response = await axios.get('http://192.168.8.49:8000/api/music')
    music.value = response.data.data || mockMusic
  } catch {
    music.value = mockMusic
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchMusic()
})
</script>

<template>
  <section id="music" class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-4xl font-bold text-center mb-12">音乐馆</h2>

      <div v-if="isLoading" class="flex justify-center">
        <div class="w-10 h-10 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div 
          v-for="song in music" 
          :key="song.id"
          class="bg-slate-800/50 rounded-xl p-4 flex items-center gap-4 border border-slate-700 hover:border-purple-500/50 transition-all cursor-pointer"
        >
          <img :src="song.cover_url" :alt="song.title" class="w-20 h-20 rounded-xl object-cover" />
          <div class="flex-1">
            <h3 class="font-bold">{{ song.title }}</h3>
            <p class="text-gray-400 text-sm">{{ song.artist }}</p>
          </div>
          <span class="text-gray-400">{{ song.duration }}</span>
        </div>
      </div>
    </div>
  </section>
</template>
