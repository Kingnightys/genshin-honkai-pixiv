<!-- src/components/HeroSection.vue -->
<script setup lang="ts">
import { ref, onMounted, computed, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isVisible = ref(false)
const activeGame = ref<'genshin' | 'starrail'>('genshin')
const mouseX = ref(0)
const mouseY = ref(0)

let animationFrameId: number | null = null

const navigateTo = (path: string) => {
  router.push(path)
}

const toggleGame = (game: 'genshin' | 'starrail') => {
  activeGame.value = game
}

const handleMouseMove = (e: MouseEvent) => {
  if (animationFrameId) return
  animationFrameId = requestAnimationFrame(() => {
    mouseX.value = (e.clientX / window.innerWidth - 0.5) * 15
    mouseY.value = (e.clientY / window.innerHeight - 0.5) * 15
    animationFrameId = null
  })
}

onMounted(() => {
  requestAnimationFrame(() => {
    isVisible.value = true
  })
  window.addEventListener('mousemove', handleMouseMove, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('mousemove', handleMouseMove)
  if (animationFrameId) {
    cancelAnimationFrame(animationFrameId)
  }
})

const stats = [
  { value: '70+', label: '可玩角色', icon: 'fa-users' },
  { value: '150+', label: '游戏资讯', icon: 'fa-newspaper' },
  { value: '800+', label: '同人作品', icon: 'fa-palette' },
  { value: '24h', label: '实时更新', icon: 'fa-clock' },
]

const features = [
  { name: '开放世界', icon: 'fa-globe', game: 'genshin' },
  { name: '元素战斗', icon: 'fa-flame', game: 'genshin' },
  { name: '元素反应', icon: 'fa-droplet', game: 'genshin' },
  { name: '元素共鸣', icon: 'fa-wind', game: 'genshin' },
  { name: '星际冒险', icon: 'fa-rocket', game: 'starrail' },
  { name: '回合策略', icon: 'fa-shield', game: 'starrail' },
  { name: '命途系统', icon: 'fa-star', game: 'starrail' },
  { name: '光锥武器', icon: 'fa-sword', game: 'starrail' },
  { name: '原声音乐', icon: 'fa-music', game: 'both' },
  { name: '精美CG', icon: 'fa-play-circle', game: 'both' },
]

const gameTitle = computed(() => activeGame.value === 'genshin' ? '原神' : '星穹铁道')
const gameDescription = computed(() => activeGame.value === 'genshin' ? '探索提瓦特大陆的七元素奇幻世界' : '踏上星际列车的银河冒险之旅')
</script>

<template>
  <section class="relative min-h-screen flex items-center justify-center pt-20 px-4 overflow-hidden" @mousemove="handleMouseMove">
    <!-- 背景装饰 -->
    <div class="absolute inset-0">
      <!-- 渐变背景 -->
      <div class="absolute inset-0" :class="activeGame === 'genshin' ? 'bg-gradient-to-br from-slate-900 via-purple-950/40 to-slate-900' : 'bg-gradient-to-br from-slate-900 via-cyan-950/40 to-slate-900'"></div>
      
      <!-- 网格背景 -->
      <div class="absolute inset-0 bg-grid opacity-15"></div>
      
      <!-- 动态粒子 -->
      <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div v-for="i in 25" :key="i" 
          class="absolute rounded-full animate-float layer-accelerate"
          :class="activeGame === 'genshin' ? 'bg-gradient-to-r from-purple-500/20 to-pink-500/20' : 'bg-gradient-to-r from-cyan-500/20 to-blue-500/20'"
          :style="{
            width: Math.random() * 12 + 6 + 'px',
            height: Math.random() * 12 + 6 + 'px',
            left: Math.random() * 100 + '%',
            top: Math.random() * 100 + '%',
            animationDelay: Math.random() * 5 + 's',
            animationDuration: Math.random() * 10 + 12 + 's'
          }"
        ></div>
        <!-- 星星粒子 -->
        <div v-for="i in 12" :key="'star-' + i" 
          class="absolute animate-twinkle layer-accelerate"
          :class="activeGame === 'genshin' ? 'text-yellow-300' : 'text-cyan-300'"
          :style="{
            left: Math.random() * 100 + '%',
            top: Math.random() * 100 + '%',
            animationDelay: Math.random() * 4 + 's',
            fontSize: Math.random() * 10 + 6 + 'px'
          }"
        >
          <i class="fa fa-star"></i>
        </div>
      </div>
      
      <!-- 游戏主题光晕 -->
      <div 
        class="absolute top-1/4 left-1/4 w-[500px] h-[500px] rounded-full blur-3xl animate-pulse-slow layer-accelerate"
        :class="activeGame === 'genshin' ? 'bg-gradient-radial from-purple-500/12 via-pink-500/08 to-transparent' : 'bg-gradient-radial from-cyan-500/12 via-blue-500/08 to-transparent'"
      ></div>
      <div 
        class="absolute bottom-1/4 right-1/4 w-[400px] h-[400px] rounded-full blur-3xl animate-pulse-slow layer-accelerate"
        :class="activeGame === 'genshin' ? 'bg-gradient-radial from-pink-500/12 via-cyan-500/08 to-transparent' : 'bg-gradient-radial from-blue-500/12 via-purple-500/08 to-transparent'"
        style="animation-delay: 3s;"
      ></div>
      
      <!-- 元素符号装饰 -->
      <div class="absolute top-10 left-10 opacity-15 pointer-events-none">
        <div class="w-14 h-14 rounded-full border-2 border-purple-500/30 flex items-center justify-center animate-spin-optimized layer-accelerate">
          <i class="fa fa-sun text-purple-400 text-xl"></i>
        </div>
      </div>
      <div class="absolute top-20 right-20 opacity-15 pointer-events-none">
        <div class="w-10 h-10 rounded-full border-2 border-cyan-500/30 flex items-center justify-center animate-spin-optimized layer-accelerate" style="animation-direction: reverse; animation-duration: 20s;">
          <i class="fa fa-star text-cyan-400 text-lg"></i>
        </div>
      </div>
      <div class="absolute bottom-20 left-20 opacity-15 pointer-events-none">
        <div class="w-12 h-12 rounded-full border-2 border-pink-500/30 flex items-center justify-center animate-spin-optimized layer-accelerate" style="animation-duration: 18s;">
          <i class="fa fa-moon text-pink-400 text-lg"></i>
        </div>
      </div>
    </div>

    <!-- 主内容 -->
    <div class="relative z-10 text-center max-w-6xl mx-auto layer-accelerate" :style="{ transform: `translate(${mouseX * 0.3}px, ${mouseY * 0.3}px)` }">
      <!-- 游戏切换 -->
      <div 
        class="flex justify-center gap-3 mb-10 transition-all duration-1000" 
        :class="isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'"
      >
        <button
          class="group relative px-8 py-3 rounded-full font-bold text-lg transition-all duration-500 flex items-center gap-3 overflow-hidden"
          :class="activeGame === 'genshin' 
            ? 'bg-gradient-to-r from-purple-600 via-pink-500 to-cyan-500 text-white shadow-2xl shadow-purple-500/40 scale-105' 
            : 'bg-white/5 hover:bg-white/10 border border-white/20 backdrop-blur-sm'"
          @click="toggleGame('genshin')"
        >
          <div class="absolute inset-0 bg-gradient-to-r from-white/0 via-white/20 to-white/0 -translate-x-full group-hover:translate-x-full transition-transform duration-700"></div>
          <div class="relative w-8 h-8 rounded-full flex items-center justify-center" :class="activeGame === 'genshin' ? 'bg-yellow-400/30' : ''">
            <i class="fa fa-sun text-yellow-300 text-lg"></i>
            <div v-if="activeGame === 'genshin'" class="absolute inset-0 rounded-full bg-yellow-400/20 animate-pulse-optimized"></div>
          </div>
          <span class="relative">原神</span>
          <div v-if="activeGame === 'genshin'" class="absolute inset-0 rounded-full border border-purple-400/50 animate-spin-optimized" style="animation-duration: 3s;"></div>
        </button>
        
        <div class="flex items-center">
          <div class="w-10 h-10 rounded-full border-2 border-dashed border-white/20 flex items-center justify-center">
            <span class="text-white/40 text-xs">+</span>
          </div>
        </div>
        
        <button
          class="group relative px-8 py-3 rounded-full font-bold text-lg transition-all duration-500 flex items-center gap-3 overflow-hidden"
          :class="activeGame === 'starrail' 
            ? 'bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-500 text-white shadow-2xl shadow-cyan-500/40 scale-105' 
            : 'bg-white/5 hover:bg-white/10 border border-white/20 backdrop-blur-sm'"
          @click="toggleGame('starrail')"
        >
          <div class="absolute inset-0 bg-gradient-to-r from-white/0 via-white/20 to-white/0 -translate-x-full group-hover:translate-x-full transition-transform duration-700"></div>
          <div class="relative w-8 h-8 rounded-full flex items-center justify-center" :class="activeGame === 'starrail' ? 'bg-cyan-400/30' : ''">
            <i class="fa fa-star text-cyan-300 text-lg"></i>
            <div v-if="activeGame === 'starrail'" class="absolute inset-0 rounded-full bg-cyan-400/20 animate-pulse-optimized"></div>
          </div>
          <span class="relative">星穹铁道</span>
          <div v-if="activeGame === 'starrail'" class="absolute inset-0 rounded-full border border-cyan-400/50 animate-spin-optimized" style="animation-duration: 3s;"></div>
        </button>
      </div>

      <!-- 主标题 -->
      <div 
        class="mb-12 transition-all duration-1000 delay-200" 
        :class="isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'"
      >
        <div class="inline-flex items-center gap-3 px-6 py-3 rounded-full mb-8 backdrop-blur-md border-2" 
          :class="activeGame === 'genshin' ? 'bg-purple-500/20 border-purple-500/40 shadow-lg shadow-purple-500/20' : 'bg-cyan-500/20 border-cyan-500/40 shadow-lg shadow-cyan-500/20'">
          <span class="relative">
            <span class="w-3 h-3 rounded-full animate-pulse-optimized" :class="activeGame === 'genshin' ? 'bg-gradient-to-r from-purple-400 to-pink-400' : 'bg-gradient-to-r from-cyan-400 to-blue-400'"></span>
          </span>
          <span :class="activeGame === 'genshin' ? 'text-purple-300' : 'text-cyan-300'" class="text-sm font-medium">
            {{ activeGame === 'genshin' ? '提瓦特大陆' : '星际世界' }}探索中
          </span>
          <span class="text-xs px-2 py-0.5 rounded-full" :class="activeGame === 'genshin' ? 'bg-purple-500/30 text-purple-200' : 'bg-cyan-500/30 text-cyan-200'">
            v4.8
          </span>
        </div>
        
        <div class="relative mb-6">
          <h1 class="text-6xl md:text-7xl lg:text-9xl font-black mb-2 leading-none">
            <span :class="activeGame === 'genshin' ? 'text-genshin-gradient' : 'text-starrail-gradient'" class="animate-gradient-text inline-block">
              {{ gameTitle }}
            </span>
          </h1>
          <div 
            class="absolute -bottom-4 left-1/2 -translate-x-1/2 w-3/4 h-3 blur-2xl" 
            :class="activeGame === 'genshin' ? 'bg-gradient-to-r from-purple-500/50 via-pink-500/50 to-cyan-500/50' : 'bg-gradient-to-r from-cyan-500/50 via-blue-500/50 to-purple-500/50'"
          ></div>
        </div>
        
        <p class="text-xl md:text-2xl lg:text-3xl text-gray-200 max-w-3xl mx-auto leading-relaxed font-light">
          <span class="bg-clip-text text-transparent" :class="activeGame === 'genshin' ? 'bg-gradient-to-r from-purple-400 via-pink-400 to-cyan-400' : 'bg-gradient-to-r from-cyan-400 via-blue-400 to-purple-400'">
            {{ gameDescription }}
          </span>
        </p>
      </div>

      <!-- 中心装饰元素 -->
      <div 
        class="relative w-72 h-72 md:w-80 md:h-80 mx-auto mb-12 transition-all duration-700 delay-300 layer-accelerate" 
        :class="isVisible ? 'opacity-100 scale-100' : 'opacity-0 scale-50'"
        :style="{ transform: `translate(${-mouseX * 0.2}px, ${-mouseY * 0.2}px)` }"
      >
        <div class="absolute inset-0 border-2 rounded-full animate-spin-optimized" 
          :class="activeGame === 'genshin' ? 'border-purple-500/25' : 'border-cyan-500/25'" 
          style="animation-duration: 30s;"></div>
        <div class="absolute inset-5 border-2 rounded-full animate-spin-optimized" 
          :class="activeGame === 'genshin' ? 'border-pink-500/25' : 'border-blue-500/25'" 
          style="animation-duration: 22s; animation-direction: reverse;"></div>
        <div class="absolute inset-10 border rounded-full animate-spin-optimized" 
          :class="activeGame === 'genshin' ? 'border-cyan-500/25' : 'border-purple-500/25'" 
          style="animation-duration: 15s;"></div>
        
        <div class="absolute top-0 left-1/2 -translate-x-1/2">
          <div class="w-3 h-3 rounded-full animate-pulse-optimized" :class="activeGame === 'genshin' ? 'bg-purple-400' : 'bg-cyan-400'"></div>
        </div>
        <div class="absolute bottom-0 left-1/2 -translate-x-1/2">
          <div class="w-2.5 h-2.5 rounded-full animate-pulse-optimized" :class="activeGame === 'genshin' ? 'bg-pink-400' : 'bg-blue-400'" style="animation-delay: 0.5s;"></div>
        </div>
        <div class="absolute left-0 top-1/2 -translate-y-1/2">
          <div class="w-2.5 h-2.5 rounded-full animate-pulse-optimized" :class="activeGame === 'genshin' ? 'bg-cyan-400' : 'bg-purple-400'" style="animation-delay: 1s;"></div>
        </div>
        <div class="absolute right-0 top-1/2 -translate-y-1/2">
          <div class="w-2 h-2 rounded-full animate-pulse-optimized" :class="activeGame === 'genshin' ? 'bg-yellow-400' : 'bg-teal-400'" style="animation-delay: 1.5s;"></div>
        </div>
        
        <div class="absolute inset-0 rounded-full blur-3xl animate-pulse-slow layer-accelerate" 
          :class="activeGame === 'genshin' ? 'bg-gradient-to-r from-purple-500/20 via-pink-500/20 to-cyan-500/20' : 'bg-gradient-to-r from-cyan-500/20 via-blue-500/20 to-purple-500/20'"
        ></div>
        
        <div class="absolute inset-0 flex items-center justify-center">
          <div class="relative">
            <div class="absolute inset-[-16px] rounded-full blur-xl layer-accelerate" 
              :class="activeGame === 'genshin' ? 'bg-gradient-to-br from-purple-500/35 via-pink-500/35 to-cyan-500/35' : 'bg-gradient-to-br from-cyan-500/35 via-blue-500/35 to-purple-500/35'"
              style="animation: pulse-optimized 3s ease-in-out infinite;">
            </div>
            <div class="relative w-24 h-24 md:w-28 md:h-28 rounded-full flex items-center justify-center shadow-xl transition-all duration-300" 
              :class="activeGame === 'genshin' 
                ? 'bg-gradient-to-br from-purple-600 via-pink-500 to-cyan-500 shadow-purple-500/50' 
                : 'bg-gradient-to-br from-cyan-500 via-blue-500 to-purple-600 shadow-cyan-500/50'"
            >
              <div class="absolute inset-1 rounded-full bg-black/15"></div>
              <div class="relative flex items-center gap-2">
                <i :class="activeGame === 'genshin' ? 'fa fa-sun text-yellow-200' : 'fa fa-star text-cyan-200'" class="text-3xl md:text-4xl"></i>
              </div>
            </div>
            <div class="absolute inset-0 rounded-full border-2 animate-spin-optimized" 
              :class="activeGame === 'genshin' ? 'border-purple-400/50' : 'border-cyan-400/50'" 
              style="animation-duration: 5s;"></div>
          </div>
        </div>
        
        <div class="absolute top-3 left-1/4 animate-float-slow opacity-50">
          <i :class="activeGame === 'genshin' ? 'fa fa-moon text-purple-400' : 'fa fa-circle text-cyan-400'" class="text-lg"></i>
        </div>
        <div class="absolute top-3 right-1/4 animate-float-slow opacity-50" style="animation-delay: 1s;">
          <i :class="activeGame === 'genshin' ? 'fa fa-star text-pink-400' : 'fa fa-star text-blue-400'" class="text-base"></i>
        </div>
        <div class="absolute bottom-3 left-1/4 animate-float-slow opacity-50" style="animation-delay: 2s;">
          <i :class="activeGame === 'genshin' ? 'fa fa-star text-cyan-400' : 'fa fa-moon text-purple-400'" class="text-base"></i>
        </div>
        <div class="absolute bottom-3 right-1/4 animate-float-slow opacity-50" style="animation-delay: 3s;">
          <i :class="activeGame === 'genshin' ? 'fa fa-circle text-yellow-400' : 'fa fa-circle text-teal-400'" class="text-lg"></i>
        </div>
      </div>

      <!-- 操作按钮 -->
      <div 
        class="flex flex-col sm:flex-row gap-4 justify-center mb-14 transition-all duration-1000 delay-400" 
        :class="isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'"
      >
        <button 
          class="group relative px-12 py-4.5 rounded-2xl font-bold text-lg hover:opacity-90 transition-all hover:scale-105 shadow-2xl overflow-hidden" 
          :class="activeGame === 'genshin' 
            ? 'bg-gradient-to-r from-purple-600 via-pink-500 to-cyan-500 shadow-purple-500/50' 
            : 'bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-600 shadow-cyan-500/50'"
          @click="navigateTo('/characters')"
        >
          <div class="absolute inset-0 bg-gradient-to-r from-white/30 via-white/10 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-700"></div>
          <div class="absolute inset-0 rounded-2xl border-2 border-white/0 group-hover:border-white/30 transition-colors duration-300"></div>
          <span class="relative flex items-center justify-center gap-3">
            <div class="w-8 h-8 rounded-full bg-white/20 flex items-center justify-center">
              <i class="fa fa-users text-white"></i>
            </div>
            探索角色
          </span>
        </button>
        
        <button 
          class="group relative px-12 py-4.5 rounded-2xl font-bold text-lg transition-all hover:scale-105 backdrop-blur-md overflow-hidden" 
          :class="activeGame === 'genshin' 
            ? 'bg-purple-500/10 border-2 border-purple-500/40 hover:bg-purple-500/20 hover:border-purple-400/60 shadow-lg shadow-purple-500/10' 
            : 'bg-cyan-500/10 border-2 border-cyan-500/40 hover:bg-cyan-500/20 hover:border-cyan-400/60 shadow-lg shadow-cyan-500/10'"
          @click="navigateTo('/banner')"
        >
          <div class="absolute inset-0 bg-gradient-to-r from-white/10 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-500"></div>
          <span class="relative flex items-center justify-center gap-3">
            <div class="w-8 h-8 rounded-full flex items-center justify-center" :class="activeGame === 'genshin' ? 'bg-purple-500/30' : 'bg-cyan-500/30'">
              <i :class="activeGame === 'genshin' ? 'fa fa-gem text-purple-300' : 'fa fa-gem text-cyan-300'"></i>
            </div>
            祈愿卡池
            <span class="px-2 py-0.5 rounded-full text-xs font-bold" :class="activeGame === 'genshin' ? 'bg-purple-500/40 text-purple-200' : 'bg-cyan-500/40 text-cyan-200'">
              UP
            </span>
          </span>
        </button>
        
        <button 
          class="group relative px-12 py-4.5 rounded-2xl font-bold text-lg transition-all hover:scale-105 backdrop-blur-md overflow-hidden" 
          :class="activeGame === 'genshin' 
            ? 'bg-pink-500/10 border-2 border-pink-500/40 hover:bg-pink-500/20 hover:border-pink-400/60 shadow-lg shadow-pink-500/10' 
            : 'bg-blue-500/10 border-2 border-blue-500/40 hover:bg-blue-500/20 hover:border-blue-400/60 shadow-lg shadow-blue-500/10'"
          @click="navigateTo('/news')"
        >
          <div class="absolute inset-0 bg-gradient-to-r from-white/10 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-500"></div>
          <span class="relative flex items-center justify-center gap-3">
            <div class="w-8 h-8 rounded-full flex items-center justify-center" :class="activeGame === 'genshin' ? 'bg-pink-500/30' : 'bg-blue-500/30'">
              <i :class="activeGame === 'genshin' ? 'fa fa-newspaper text-pink-300' : 'fa fa-newspaper text-blue-300'"></i>
            </div>
            最新资讯
            <span class="px-2 py-0.5 rounded-full text-xs font-bold bg-red-500/60 text-red-200 animate-pulse-optimized">
              Hot
            </span>
          </span>
        </button>
      </div>

      <!-- 统计数据 -->
      <div 
        class="grid grid-cols-2 md:grid-cols-4 gap-5 max-w-4xl mx-auto transition-all duration-1000 delay-500" 
        :class="isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'"
      >
        <div 
          v-for="stat in stats" 
          :key="stat.label" 
          class="group relative p-5 rounded-2xl border backdrop-blur-md transition-all duration-300 hover:-translate-y-2 hover:shadow-xl"
          :class="activeGame === 'genshin' 
            ? 'bg-purple-500/5 border-purple-500/20 hover:bg-purple-500/10 hover:border-purple-500/40 hover:shadow-purple-500/20' 
            : 'bg-cyan-500/5 border-cyan-500/20 hover:bg-cyan-500/10 hover:border-cyan-500/40 hover:shadow-cyan-500/20'"
        >
          <div 
            class="absolute inset-0 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300" 
            :class="activeGame === 'genshin' ? 'bg-gradient-to-br from-purple-500/10 to-transparent' : 'bg-gradient-to-br from-cyan-500/10 to-transparent'"
          ></div>
          <div class="relative">
            <div 
              class="w-12 h-12 mx-auto rounded-xl flex items-center justify-center mb-3 transition-transform duration-300 group-hover:scale-110" 
              :class="activeGame === 'genshin' ? 'bg-purple-500/20' : 'bg-cyan-500/20'"
            >
              <i :class="[`fa ${stat.icon} text-xl`, activeGame === 'genshin' ? 'text-purple-400' : 'text-cyan-400']"></i>
            </div>
            <div 
              class="text-3xl font-black mb-1 transition-transform duration-300 group-hover:scale-110" 
              :class="activeGame === 'genshin' ? 'text-genshin-gradient' : 'text-starrail-gradient'"
            >
              {{ stat.value }}
            </div>
            <div class="text-gray-400 text-sm">{{ stat.label }}</div>
          </div>
        </div>
      </div>

      <!-- 特色标签 -->
      <div 
        class="flex flex-wrap justify-center gap-3 mt-14 transition-all duration-1000 delay-700" 
        :class="isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'"
      >
        <span 
          v-for="feature in features" 
          :key="feature.name"
          class="group relative px-6 py-3 rounded-full text-sm font-medium hover:scale-110 transition-all duration-300 cursor-pointer border-2 overflow-hidden"
          :class="feature.game === 'both' 
            ? 'bg-white/10 border-white/20 text-gray-300 hover:bg-white/20 hover:border-white/40' 
            : (feature.game === 'genshin' 
                ? 'bg-purple-500/15 border-purple-500/30 text-purple-300 hover:bg-purple-500/30 hover:border-purple-500/50 hover:shadow-lg hover:shadow-purple-500/20' 
                : 'bg-cyan-500/15 border-cyan-500/30 text-cyan-300 hover:bg-cyan-500/30 hover:border-cyan-500/50 hover:shadow-lg hover:shadow-cyan-500/20')"
        >
          <div class="absolute inset-0 bg-gradient-to-r from-white/0 via-white/10 to-white/0 -translate-x-full group-hover:translate-x-full transition-transform duration-500"></div>
          <span class="relative flex items-center gap-2">
            <i :class="`fa ${feature.icon} text-base`"></i>
            {{ feature.name }}
          </span>
        </span>
      </div>
      
      <!-- 底部装饰线 -->
      <div class="mt-16 max-w-4xl mx-auto">
        <div class="flex items-center justify-center gap-4">
          <div class="h-px flex-1 bg-gradient-to-r from-transparent via-purple-500/50 to-transparent"></div>
          <div class="w-3 h-3 rounded-full animate-pulse-optimized" :class="activeGame === 'genshin' ? 'bg-purple-500' : 'bg-cyan-500'"></div>
          <div class="h-px flex-1 bg-gradient-to-r from-transparent via-cyan-500/50 to-transparent"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
</style>