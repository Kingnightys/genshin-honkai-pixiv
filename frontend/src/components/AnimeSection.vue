<script setup lang="ts">
import { ref } from 'vue'

interface Anime {
  id: number
  title: string
  description: string
  image: string
  episode: number
}

const animes = ref<Anime[]>([
  { id: 1, title: '原神', description: '旅行者的冒险故事', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20anime%20poster&width=300&height=200', episode: 12 },
  { id: 2, title: '星穹铁道', description: '星际探索之旅', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20anime%20poster&width=300&height=200', episode: 8 },
])
</script>

<template>
  <section id="anime" class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-4xl font-bold text-center mb-12">番剧馆</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div 
          v-for="anime in animes" 
          :key="anime.id"
          class="bg-slate-800/50 rounded-xl overflow-hidden border border-slate-700 hover:border-purple-500/50 transition-all cursor-pointer"
        >
          <img :src="anime.image" :alt="anime.title" class="w-full h-40 object-cover" />
          <div class="p-4">
            <h3 class="font-bold text-lg">{{ anime.title }}</h3>
            <p class="text-gray-400 text-sm mb-2">{{ anime.description }}</p>
            <span class="text-xs text-purple-400">{{ anime.episode }} 集</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
