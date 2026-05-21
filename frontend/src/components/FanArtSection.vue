<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface FanArt {
  id: number
  title: string
  image: string
  author: string
}

const fanarts = ref<FanArt[]>([])
const isLoading = ref(true)

// Mock数据
const mockFanarts: FanArt[] = [
  { id: 1, title: '原神壁纸', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20fan%20art%20wallpaper&width=250&height=250', author: '画师A' },
  { id: 2, title: '星穹铁道', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20fan%20art&width=250&height=250', author: '画师B' },
  { id: 3, title: '角色合集', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20honkai%20character%20fan%20art&width=250&height=250', author: '画师C' },
]

const fetchFanArts = async () => {
  try {
    const response = await axios.get('http://192.168.8.49:8000/api/fanarts')
    fanarts.value = response.data.data || mockFanarts
  } catch {
    fanarts.value = mockFanarts
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchFanArts()
})
</script>

<template>
  <section id="fanart" class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-4xl font-bold text-center mb-12">同人汇</h2>

      <div v-if="isLoading" class="flex justify-center">
        <div class="w-10 h-10 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
        <div 
          v-for="art in fanarts" 
          :key="art.id"
          class="bg-slate-800/50 rounded-xl overflow-hidden border border-slate-700 hover:border-purple-500/50 transition-all cursor-pointer group"
        >
          <img :src="art.image" :alt="art.title" class="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-300" />
          <div class="p-3">
            <h4 class="font-bold text-sm">{{ art.title }}</h4>
            <p class="text-xs text-gray-400">{{ art.author }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
