<script setup lang="ts">
import { ref } from 'vue'

interface MapSpot {
  id: number
  name: string
  description: string
  image: string
}

const spots = ref<MapSpot[]>([
  { id: 1, name: '蒙德城', description: '自由之都', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=mondstadt%20city%20genshin&width=200&height=150' },
  { id: 2, name: '璃月港', description: '契约之城', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=liyue%20harbor%20genshin&width=200&height=150' },
  { id: 3, name: '稻妻城', description: '永恒之地', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=inazuma%20city%20genshin&width=200&height=150' },
])
</script>

<template>
  <section id="map" class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-4xl font-bold text-center mb-12">地图打卡</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div 
          v-for="spot in spots" 
          :key="spot.id"
          class="bg-slate-800/50 rounded-xl overflow-hidden border border-slate-700 hover:border-purple-500/50 transition-all cursor-pointer"
        >
          <img :src="spot.image" :alt="spot.name" class="w-full h-32 object-cover" />
          <div class="p-4">
            <h3 class="font-bold text-lg">{{ spot.name }}</h3>
            <p class="text-gray-400 text-sm">{{ spot.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
