<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import Navbar from './components/NavbarSection.vue'
import HeroSection from './components/HeroSection.vue'
import BannerSection from './components/BannerSection.vue'
import CharacterSection from './components/CharacterSection.vue'
import ActivitiesSection from './components/ActivitiesSection.vue'
import NewsSection from './components/NewsSection.vue'
import MusicSection from './components/MusicSection.vue'
import PvSection from './components/PvSection.vue'
import FanArtSection from './components/FanArtSection.vue'
import MapSection from './components/MapSection.vue'
import AnimeSection from './components/AnimeSection.vue'
import PlayerSearch from './components/PlayerSearch.vue'
import MessageSection from './components/MessageSection.vue'
import Footer from './components/Footer.vue'

// 轮播背景
const backgrounds = [
  'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20fantasy%20landscape%20anime&width=1920&height=1080',
  'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20space%20station%20anime&width=1920&height=1080',
  'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20liyue%20city%20chinese%20architecture&width=1920&height=1080',
  'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20planet%20surface%20fantasy&width=1920&height=1080'
]

const currentBgIndex = ref(0)
let bgInterval: number | null = null

const nextBackground = () => {
  currentBgIndex.value = (currentBgIndex.value + 1) % backgrounds.length
}

onMounted(() => {
  bgInterval = window.setInterval(nextBackground, 5000)
})

onUnmounted(() => {
  if (bgInterval) clearInterval(bgInterval)
})
</script>

<template>
  <div class="min-h-screen bg-slate-900 text-white overflow-x-hidden">
    <!-- 轮播背景 -->
    <div class="fixed inset-0 z-0">
      <div
        v-for="(bg, index) in backgrounds"
        :key="index"
        class="absolute inset-0 bg-cover bg-center transition-opacity duration-1000"
        :class="currentBgIndex === index ? 'opacity-100' : 'opacity-0'"
        :style="{ backgroundImage: `url(${bg})` }"
      ></div>
      <div class="absolute inset-0 bg-gradient-to-b from-black/60 via-black/40 to-slate-900"></div>
    </div>

    <!-- 导航栏 -->
    <Navbar />

    <!-- 主内容 -->
    <main class="relative z-10">
      <HeroSection />
      <BannerSection />
      <CharacterSection />
      <ActivitiesSection />
      <NewsSection />
      <MusicSection />
      <PvSection />
      <FanArtSection />
      <MapSection />
      <AnimeSection />
      <PlayerSearch />
      <MessageSection />
    </main>

    <!-- 页脚 -->
    <Footer />
  </div>
</template>
