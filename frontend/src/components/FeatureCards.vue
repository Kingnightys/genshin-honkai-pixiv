<script setup lang="ts">
import { ref } from 'vue'

const features = ref([
  {
    icon: '🎭',
    title: '角色图鉴',
    description: '收录原神与星穹铁道所有角色，从开服至今完整呈现',
    link: '#characters',
    stats: '70+',
    gradient: 'from-purple-500 to-pink-500'
  },
  {
    icon: '🎵',
    title: '音乐馆',
    description: '聆听HOYO-MiX精心制作的游戏原声音乐',
    link: '#music',
    stats: '20+',
    gradient: 'from-blue-500 to-cyan-500'
  },
  {
    icon: '🎬',
    title: 'PV展览',
    description: '回顾每一个震撼人心的版本预告',
    link: '#pv',
    stats: '10+',
    gradient: 'from-green-500 to-emerald-500'
  },
  {
    icon: '🗺️',
    title: '地图探索',
    description: '探索提瓦特大陆与星际航线的美景',
    link: '#map',
    stats: '5+',
    gradient: 'from-orange-500 to-amber-500'
  }
])

const hoveredIndex = ref<number | null>(null)

const navigateTo = (link: string) => {
  const element = document.querySelector(link)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>

<template>
  <section class="py-20 px-4 bg-gradient-to-b from-dark via-slate-900/50 to-dark">
    <div class="max-w-7xl mx-auto">
      <div class="text-center mb-16">
        <span class="inline-block px-4 py-1.5 bg-primary/10 text-primary rounded-full text-sm font-medium mb-4">
          精彩内容
        </span>
        <h2 class="text-4xl md:text-5xl font-bold mb-4">探索游戏世界</h2>
        <p class="text-gray-400 max-w-2xl mx-auto text-lg">丰富的游戏内容，一站式体验提瓦特与银河的魅力</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div
          v-for="(feature, index) in features"
          :key="index"
          class="group relative bg-slate-800/40 backdrop-blur-sm rounded-2xl p-6 border border-slate-700/50 cursor-pointer transform transition-all duration-500"
          :class="[
            hoveredIndex === index 
              ? 'hover:-translate-y-3 hover:shadow-2xl hover:border-transparent' 
              : 'hover:-translate-y-2',
            hoveredIndex === index ? `hover:shadow-${feature.gradient.split('-')[1]}-500/20` : ''
          ]"
          @mouseenter="hoveredIndex = index"
          @mouseleave="hoveredIndex = null"
          @click="navigateTo(feature.link)"
        >
          <!-- 背景渐变光效 -->
          <div 
            class="absolute inset-0 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 bg-gradient-to-br"
            :class="feature.gradient"
            style="filter: blur(40px); transform: scale(0.8); group-hover:scale(1); transition: transform 0.5s;"
          ></div>
          
          <div class="relative z-10">
            <!-- 图标 -->
            <div 
              class="w-14 h-14 rounded-xl flex items-center justify-center text-3xl mb-5 transition-all duration-300"
              :class="[
                hoveredIndex === index 
                  ? `bg-gradient-to-br ${feature.gradient} text-white scale-110` 
                  : 'bg-slate-700/50'
              ]"
            >
              {{ feature.icon }}
            </div>
            
            <!-- 标题和统计 -->
            <div class="flex items-center justify-between mb-3">
              <h3 class="text-xl font-bold text-white">{{ feature.title }}</h3>
              <span 
                class="px-2.5 py-1 rounded-full text-xs font-semibold transition-all duration-300"
                :class="[
                  hoveredIndex === index 
                    ? `bg-gradient-to-r ${feature.gradient} text-white` 
                    : 'bg-slate-700 text-gray-300'
                ]"
              >
                {{ feature.stats }}
              </span>
            </div>
            
            <!-- 描述 -->
            <p class="text-gray-400 text-sm leading-relaxed mb-4">
              {{ feature.description }}
            </p>
            
            <!-- 链接按钮 -->
            <div 
              class="inline-flex items-center gap-2 text-sm font-medium transition-all duration-300"
              :class="[
                hoveredIndex === index 
                  ? 'text-white' 
                  : 'text-primary opacity-0 group-hover:opacity-100'
              ]"
            >
              <span>立即探索</span>
              <i class="fa fa-arrow-right transition-transform duration-300" :class="{ 'translate-x-1': hoveredIndex === index }"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hover\:shadow-purple-500\/20:hover {
  box-shadow: 0 0 40px rgba(168, 85, 247, 0.2);
}

.hover\:shadow-blue-500\/20:hover {
  box-shadow: 0 0 40px rgba(59, 130, 246, 0.2);
}

.hover\:shadow-green-500\/20:hover {
  box-shadow: 0 0 40px rgba(34, 197, 94, 0.2);
}

.hover\:shadow-orange-500\/20:hover {
  box-shadow: 0 0 40px rgba(249, 115, 22, 0.2);
}
</style>