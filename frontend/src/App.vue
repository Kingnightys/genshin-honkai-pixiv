<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'
import Navbar from './components/NavbarSection.vue'
import Footer from './components/Footer.vue'

// 游戏状态共享
const activeGame = ref<'genshin' | 'starrail'>('genshin')

// 背景轮播
const backgrounds = [
  { url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20mondstadt%20city%20fantasy%20sky%20anime%20style%20beautiful&width=1920&height=1080', game: 'genshin' },
  { url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20astral%20express%20space%20train%20futuristic%20anime&width=1920&height=1080', game: 'starrail' },
  { url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20liyue%20harbor%20chinese%20architecture%20night%20lanterns%20anime&width=1920&height=1080', game: 'genshin' },
  { url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20belobog%20city%20snow%20winter%20fantasy%20anime&width=1920&height=1080', game: 'starrail' },
  { url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20inazuma%20island%20japanese%20castle%20ocean%20anime&width=1920&height=1080', game: 'genshin' },
  { url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20penacony%20casino%20neon%20lights%20futuristic&width=1920&height=1080', game: 'starrail' }
]

const currentBgIndex = ref(0)
let bgInterval: number | null = null

const currentBgGame = computed(() => backgrounds[currentBgIndex.value]?.game)

const nextBackground = () => {
  currentBgIndex.value = (currentBgIndex.value + 1) % backgrounds.length
}

const setActiveGame = (game: 'genshin' | 'starrail') => {
  activeGame.value = game
}

onMounted(() => {
  bgInterval = window.setInterval(nextBackground, 10000)
})

onUnmounted(() => {
  if (bgInterval) clearInterval(bgInterval)
})
</script>

<template>
  <div class="min-h-screen screen-padding bg-slate-900 text-white overflow-x-hidden">
    <!-- 动态背景层 -->
    <div class="fixed inset-0 z-0">
      <!-- 背景图片 -->
      <div v-for="(bg, index) in backgrounds" :key="index"
        class="absolute inset-0 bg-cover bg-center transition-all duration-2000"
        :class="currentBgIndex === index ? 'opacity-100 scale-105' : 'opacity-0 scale-100'"
        :style="{ backgroundImage: `url(${bg.url})` }"></div>

      <!-- 动态渐变遮罩 -->
      <div class="absolute inset-0 bg-gradient-to-b from-slate-900/90 via-slate-900/60 to-slate-900"></div>

      <!-- 游戏主题光晕 -->
      <div class="absolute inset-0 transition-all duration-2000" :class="currentBgGame === 'genshin'
        ? 'bg-gradient-to-br from-purple-900/25 via-pink-900/15 to-transparent'
        : 'bg-gradient-to-br from-cyan-900/25 via-blue-900/15 to-transparent'"></div>

      <!-- 网格背景效果 -->
      <div class="absolute inset-0 bg-grid opacity-20"></div>

      <!-- 动态粒子效果 -->
      <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div v-for="i in 30" :key="i" class="absolute rounded-full animate-float layer-accelerate" :class="currentBgGame === 'genshin'
          ? 'bg-gradient-to-r from-purple-500/20 to-pink-500/20'
          : 'bg-gradient-to-r from-cyan-500/20 to-blue-500/20'" :style="{
              width: Math.random() * 12 + 6 + 'px',
              height: Math.random() * 12 + 6 + 'px',
              left: Math.random() * 100 + '%',
              top: Math.random() * 100 + '%',
              animationDelay: Math.random() * 5 + 's',
              animationDuration: Math.random() * 10 + 10 + 's'
            }"></div>
        <!-- 星星粒子 -->
        <div v-for="i in 15" :key="'star-' + i" class="absolute animate-twinkle layer-accelerate"
          :class="currentBgGame === 'genshin' ? 'text-yellow-300' : 'text-cyan-300'" :style="{
            left: Math.random() * 100 + '%',
            top: Math.random() * 100 + '%',
            animationDelay: Math.random() * 4 + 's',
            fontSize: Math.random() * 10 + 6 + 'px'
          }">
          <i class="fa fa-star"></i>
        </div>
      </div>
    </div>
    <!-- 导航栏 -->
    <Navbar />
    <!-- 当前游戏标识 -->
    <div class="fixed top-24 left-4 z-20 hidden lg:block">
      <div class="px-3 py-1.5 rounded-full text-xs font-medium backdrop-blur-sm border transition-all duration-500"
        :class="currentBgGame === 'genshin'
          ? 'bg-purple-500/20 border-purple-500/30 text-purple-300'
          : 'bg-cyan-500/20 border-cyan-500/30 text-cyan-300'">
        <span class="flex items-center gap-1.5">
          <i :class="currentBgGame === 'genshin' ? 'fa fa-sun' : 'fa fa-star'"></i>
          {{ currentBgGame === 'genshin' ? '原神' : '星穹铁道' }}
        </span>
      </div>
    </div>

    <!-- 主内容区域 -->
    <main class="relative z-10 min-h-screen">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- 页脚 -->
    <Footer />
  </div>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.screen-padding {
  padding-top: 4.5rem;
}
</style>
