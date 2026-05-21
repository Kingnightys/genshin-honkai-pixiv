<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface NewsItem {
  id: number
  title: string
  content: string
  image: string
  time: string
}

const news = ref<NewsItem[]>([])
const isLoading = ref(true)

// Mock数据
const mockNews: NewsItem[] = [
  { id: 1, title: '原神4.0版本更新', content: '全新地区枫丹上线', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20fontaine%20update&width=300&height=150', time: '2024-08-14' },
  { id: 2, title: '星穹铁道1.6版本', content: '新角色和新剧情', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20update&width=300&height=150', time: '2024-08-10' },
  { id: 3, title: '原神音乐会', content: 'HOYO-MiX现场演出', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20concert%20poster&width=300&height=150', time: '2024-08-08' },
]

const fetchNews = async () => {
  try {
    const response = await axios.get('http://192.168.8.49:8000/api/news/genshin')
    news.value = response.data.data || mockNews
  } catch {
    news.value = mockNews
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchNews()
})
</script>

<template>
  <section id="news" class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-4xl font-bold text-center mb-12">最新资讯</h2>

      <div v-if="isLoading" class="flex justify-center">
        <div class="w-10 h-10 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div 
          v-for="item in news" 
          :key="item.id"
          class="bg-slate-800/50 rounded-xl overflow-hidden border border-slate-700 hover:border-purple-500/50 transition-all cursor-pointer"
        >
          <img :src="item.image" :alt="item.title" class="w-full h-24 object-cover" />
          <div class="p-4">
            <h3 class="font-bold text-lg mb-2">{{ item.title }}</h3>
            <p class="text-gray-400 text-sm mb-3">{{ item.content }}</p>
            <span class="text-xs text-gray-500">{{ item.time }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
