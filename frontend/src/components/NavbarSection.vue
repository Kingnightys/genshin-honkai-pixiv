<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const isScrolled = ref(false)
const isMobileMenuOpen = ref(false)

const navItems = [
  { href: '#home', label: '首页' },
  { href: '#banner', label: '卡池' },
  { href: '#characters', label: '角色' },
  { href: '#activities', label: '活动' },
  { href: '#news', label: '资讯' },
  { href: '#music', label: '音乐' },
  { href: '#pv', label: 'PV' },
  { href: '#fanart', label: '同人' },
  { href: '#map', label: '地图' },
  { href: '#anime', label: '番剧' },
  { href: '#search', label: 'UID' },
  { href: '#message', label: '留言' }
]

const scrollToSection = (href: string) => {
  isMobileMenuOpen.value = false
  const element = document.querySelector(href)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <nav 
    class="fixed top-0 left-0 right-0 z-50 transition-all duration-300"
    :class="isScrolled ? 'bg-slate-900/95 backdrop-blur-md' : 'bg-transparent'"
  >
    <div class="max-w-7xl mx-auto px-4">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-gradient-to-r from-purple-500 to-blue-500 rounded-xl flex items-center justify-center">
            <i class="fa fa-gamepad"></i>
          </div>
          <span class="text-xl font-bold bg-gradient-to-r from-purple-400 to-blue-400 bg-clip-text text-transparent">
            原神/星穹铁道
          </span>
        </div>

        <div class="hidden md:flex items-center gap-1">
          <button
            v-for="item in navItems"
            :key="item.href"
            class="px-4 py-2 rounded-lg hover:bg-white/10 transition-colors"
            @click="scrollToSection(item.href)"
          >
            {{ item.label }}
          </button>
        </div>

        <button 
          class="md:hidden p-2"
          @click="isMobileMenuOpen = !isMobileMenuOpen"
        >
          <i class="fa fa-bars"></i>
        </button>
      </div>

      <div v-if="isMobileMenuOpen" class="md:hidden pb-4 border-t border-slate-700">
        <button
          v-for="item in navItems"
          :key="item.href"
          class="block w-full text-left px-4 py-3 hover:bg-white/10 rounded-lg"
          @click="scrollToSection(item.href)"
        >
          {{ item.label }}
        </button>
      </div>
    </div>
  </nav>
</template>
