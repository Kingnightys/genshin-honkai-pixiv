<!-- d:\AiCodeProject\genshin-honkai-pixiv\frontend\src\views/HomeView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import HeroSection from '@/components/HeroSection.vue'
import BannerSection from '@/components/BannerSection.vue'
import CharacterSection from '@/components/CharacterSection.vue'
import NewsSection from '@/components/NewsSection.vue'
import MusicSection from '@/components/MusicSection.vue'

const router = useRouter()

const quickLinks = [
  { name: '角色图鉴', route: '/characters', icon: 'fa-users', color: 'from-purple-500 via-pink-500 to-blue-500' },
  { name: '祈愿卡池', route: '/banner', icon: 'fa-gem', color: 'from-pink-500 via-red-500 to-orange-500' },
  { name: '游戏资讯', route: '/news', icon: 'fa-newspaper', color: 'from-blue-500 via-cyan-500 to-teal-500' },
  { name: '音乐专辑', route: '/music', icon: 'fa-music', color: 'from-green-500 via-emerald-500 to-cyan-500' },
  { name: '同人作品', route: '/fanart', icon: 'fa-palette', color: 'from-orange-500 via-amber-500 to-yellow-500' },
  { name: '地图探索', route: '/map', icon: 'fa-map', color: 'from-cyan-500 via-blue-500 to-purple-500' }
]

const navigateTo = (route: string) => {
  router.push(route)
}
</script>

<template>
  <div class="space-y-20">
    <!-- Hero区域 -->
    <HeroSection />

    <!-- 快捷入口 -->
    <section class="py-16 px-4">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-12">
          <h2 class="text-3xl lg:text-4xl font-bold mb-4">
            <span class="bg-gradient-to-r from-purple-400 via-pink-400 to-blue-400 bg-clip-text text-transparent">
              快速导航
            </span>
          </h2>
          <p class="text-gray-400">探索您感兴趣的内容</p>
        </div>
        
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4 lg:gap-6">
          <button
            v-for="(link, index) in quickLinks"
            :key="link.name"
            class="group relative p-4 lg:p-6 rounded-2xl bg-white/5 backdrop-blur-sm border border-white/10 hover:border-white/30 transition-all duration-500 hover:scale-105 hover:-translate-y-1"
            :style="{ animationDelay: `${index * 100}ms` }"
            @click="navigateTo(link.route)"
          >
            <!-- 背景渐变光效 -->
            <div :class="`absolute inset-0 rounded-2xl bg-gradient-to-br ${link.color} opacity-0 group-hover:opacity-10 transition-opacity duration-300`"></div>
            
            <!-- 图标 -->
            <div :class="`w-12 h-12 mx-auto mb-3 lg:mb-4 rounded-xl bg-gradient-to-br ${link.color} flex items-center justify-center shadow-lg transition-transform duration-300 group-hover:scale-110`">
              <i :class="`fa ${link.icon} text-white text-lg lg:text-xl`"></i>
            </div>
            
            <!-- 文字 -->
            <span class="text-sm lg:text-base font-medium text-center block">{{ link.name }}</span>
            
            <!-- 悬浮光晕效果 -->
            <div :class="`absolute inset-0 rounded-2xl bg-gradient-to-br ${link.color} opacity-0 group-hover:opacity-20 blur-xl transition-opacity duration-500`"></div>
          </button>
        </div>
      </div>
    </section>

    <!-- 卡池预览 -->
    <BannerSection />

    <!-- 角色预览 -->
    <CharacterSection />

    <!-- 资讯预览 -->
    <NewsSection />

    <!-- 音乐预览 -->
    <MusicSection />
  </div>
</template>