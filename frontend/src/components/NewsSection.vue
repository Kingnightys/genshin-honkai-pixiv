<script setup lang="ts">
import { ref, onMounted } from 'vue'
import getNews from '@/api'

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
  { id: 1, title: '原神4.0版本更新', content: '全新地区枫丹上线，探索水下世界的奥秘', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20fontaine%20city%20underwater%20fantasy%20anime&width=600&height=300', time: '2024-08-14' },
  { id: 2, title: '星穹铁道1.6版本', content: '新角色阮·梅登场，开拓全新剧情篇章', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20new%20character%20space%20anime&width=600&height=300', time: '2024-08-10' },
  { id: 3, title: '原神音乐会2024', content: 'HOYO-MiX全球巡演即将开启', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20concert%20stage%20lights%20orchestra&width=600&height=300', time: '2024-08-08' },
]

const fetchNews = async () => {
  try {
    const res = await getNews('genshin')
    const data = Array.isArray(res?.data) ? res.data : []
    news.value = data.length > 0 ? data : mockNews
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
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h2 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-blue-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent">
            最新资讯
          </span>
        </h2>
        <p class="text-gray-400">获取原神与星穹铁道的最新动态</p>
      </div>

      <div v-if="isLoading" class="flex justify-center py-12">
        <div class="w-12 h-12 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="(item, index) in news" 
          :key="item.id"
          class="group relative bg-slate-800/50 backdrop-blur-sm rounded-2xl overflow-hidden border border-slate-700/50 hover:border-purple-500/50 transition-all duration-300 cursor-pointer hover:shadow-xl hover:shadow-purple-500/10"
          :class="index === 0 ? 'lg:col-span-2' : ''"
        >
          <div class="relative overflow-hidden" :class="index === 0 ? 'h-48' : 'h-36'">
            <img 
              :src="item.image" 
              :alt="item.title" 
              class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/50 to-transparent"></div>
            <!-- 资讯标签 -->
            <span class="absolute top-3 left-3 px-3 py-1 bg-gradient-to-r from-purple-500 to-blue-500 rounded-full text-xs font-medium">
              最新
            </span>
          </div>
          <div class="p-5">
            <div class="flex items-center gap-2 mb-3">
              <i class="fa fa-calendar text-gray-400 text-sm"></i>
              <span class="text-gray-400 text-sm">{{ item.time }}</span>
            </div>
            <h3 class="font-bold text-lg mb-2 text-white group-hover:text-purple-300 transition-colors">
              {{ item.title }}
            </h3>
            <p class="text-gray-400 text-sm line-clamp-2">{{ item.content }}</p>
            <!-- 阅读更多指示 -->
            <div class="mt-4 flex items-center gap-2 text-purple-400 text-sm opacity-0 group-hover:opacity-100 transition-opacity">
              <span>阅读更多</span>
              <i class="fa fa-arrow-right"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>