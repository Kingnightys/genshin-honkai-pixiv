<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

interface Banner {
  id: number
  name: string
  type: string
  version: string
  image: string
  game: string
}

const activeGame = ref<'genshin' | 'starrail'>('genshin')
const banners = ref<Banner[]>([])
const isLoading = ref(true)

// Mock数据 - 原神
const genshinBanners: Banner[] = [
  { id: 1, name: '芙宁娜', type: '角色', version: '4.2', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=furina%20genshin%20impact%20banner%20art%20anime%20style%20water%20element&width=400&height=500', game: 'genshin' },
  { id: 2, name: '那维莱特', type: '角色', version: '4.1', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=neuvillette%20genshin%20impact%20banner%20art%20anime%20style%20hydro&width=400&height=500', game: 'genshin' },
  { id: 3, name: '武器祈愿', type: '武器', version: '4.2', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20weapon%20banner%20art%20sword%20fantasy&width=400&height=500', game: 'genshin' },
]

// Mock数据 - 星穹铁道
const starrailBanners: Banner[] = [
  { id: 4, name: '阮·梅', type: '角色', version: '1.6', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=ruan%20mei%20honkai%20star%20rail%20banner%20art%20anime%20style&width=400&height=500', game: 'starrail' },
  { id: 5, name: '刃', type: '角色', version: '1.5', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=blade%20honkai%20star%20rail%20banner%20art%20anime%20style&width=400&height=500', game: 'starrail' },
  { id: 6, name: '光锥祈愿', type: '光锥', version: '1.6', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20light%20cone%20banner%20art%20fantasy&width=400&height=500', game: 'starrail' },
]

const fetchBanners = async () => {
  isLoading.value = true
  // 模拟API调用延迟
  await new Promise(resolve => setTimeout(resolve, 500))
  banners.value = activeGame.value === 'genshin' ? genshinBanners : starrailBanners
  isLoading.value = false
}

const navigateToBanner = () => {
  router.push('/banner')
}

onMounted(() => {
  fetchBanners()
})
</script>

<template>
  <section id="banner" class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题 -->
      <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-12">
        <div>
          <h2 class="text-4xl font-bold mb-2">
            <span class="bg-gradient-to-r from-pink-400 via-purple-400 to-blue-400 bg-clip-text text-transparent">
              祈愿卡池
            </span>
          </h2>
          <p class="text-gray-400">查看当前UP角色与武器</p>
        </div>
        
        <!-- 游戏切换 -->
        <div class="flex gap-3 mt-4 md:mt-0">
          <button 
            class="px-6 py-2 rounded-lg font-medium transition-all duration-300" 
            :class="activeGame === 'genshin' ? 'bg-gradient-to-r from-purple-500 to-blue-500' : 'bg-slate-800 hover:bg-slate-700 border border-slate-600'"
            @click="activeGame = 'genshin'; fetchBanners()"
          >
            <span class="flex items-center gap-2">
              <i class="fa fa-sun"></i> 原神
            </span>
          </button>
          <button 
            class="px-6 py-2 rounded-lg font-medium transition-all duration-300" 
            :class="activeGame === 'starrail' ? 'bg-gradient-to-r from-cyan-500 to-blue-500' : 'bg-slate-800 hover:bg-slate-700 border border-slate-600'"
            @click="activeGame = 'starrail'; fetchBanners()"
          >
            <span class="flex items-center gap-2">
              <i class="fa fa-star"></i> 星穹铁道
            </span>
          </button>
        </div>
      </div>
      
      <div v-if="isLoading" class="flex justify-center py-12">
        <div class="w-12 h-12 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="banner in banners" 
          :key="banner.id"
          class="group relative bg-slate-800/50 backdrop-blur-sm rounded-2xl overflow-hidden border border-slate-700/50 hover:border-purple-500/50 transition-all duration-300 cursor-pointer hover:shadow-xl hover:shadow-purple-500/15 hover:-translate-y-2"
          @click="navigateToBanner"
        >
          <!-- 卡池图片 -->
          <div class="relative h-72 overflow-hidden">
            <img 
              :src="banner.image" 
              :alt="banner.name" 
              class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent"></div>
            
            <!-- 5星标识 -->
            <div class="absolute top-3 left-3">
              <div class="w-8 h-8 rounded-full bg-gradient-to-br from-yellow-400 to-orange-500 flex items-center justify-center shadow-lg">
                <span class="text-xs font-bold">★</span>
              </div>
            </div>
            
            <!-- 类型标签 -->
            <span class="absolute top-3 right-3 px-3 py-1 bg-gradient-to-r from-purple-500/90 to-blue-500/90 rounded-full text-xs font-medium backdrop-blur-sm">
              {{ banner.type }}
            </span>
          </div>
          
          <!-- 信息区域 -->
          <div class="p-5">
            <div class="flex items-center justify-between mb-2">
              <span class="text-gray-400 text-sm flex items-center gap-1">
                <i class="fa fa-calendar"></i> 版本 {{ banner.version }}
              </span>
              <span class="text-xs text-purple-400">点击查看详情</span>
            </div>
            <h3 class="text-xl font-bold text-white group-hover:text-purple-300 transition-colors">
              {{ banner.name }}
            </h3>
            <!-- 祈愿按钮 -->
            <button class="mt-4 w-full py-2 bg-gradient-to-r from-purple-500/20 to-blue-500/20 border border-purple-500/30 rounded-lg text-purple-300 text-sm hover:from-purple-500/30 hover:to-blue-500/30 transition-all">
              前往祈愿
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>