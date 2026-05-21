<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getMusic } from '@/api'

interface Music {
  id: number
  title: string
  artist: string
  album: string
  cover_url: string
  duration: string
  game: string
}

const music = ref<Music[]>([])
const isLoading = ref(true)
const playingId = ref<number | null>(null)

// Mock数据
const mockMusic: Music[] = [
  { id: 1, title: '璃月', artist: 'HOYO-MiX', album: '原神OST', cover_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=liyue%20chinese%20landscape%20album%20cover%20anime&width=300&height=300', duration: '4:32', game: 'genshin' },
  { id: 2, title: '稻妻', artist: 'HOYO-MiX', album: '原神OST', cover_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=inazuma%20japanese%20landscape%20album%20cover%20anime&width=300&height=300', duration: '5:18', game: 'genshin' },
  { id: 3, title: '枫丹', artist: 'HOYO-MiX', album: '原神OST', cover_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=fontaine%20french%20city%20album%20cover%20anime&width=300&height=300', duration: '4:45', game: 'genshin' },
  { id: 4, title: '星穹铁道', artist: 'HOYO-MiX', album: '星穹铁道OST', cover_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20space%20station%20album%20cover&width=300&height=300', duration: '3:45', game: 'starrail' },
  { id: 5, title: '贝洛伯格', artist: 'HOYO-MiX', album: '星穹铁道OST', cover_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=belobog%20snow%20city%20album%20cover%20anime&width=300&height=300', duration: '4:12', game: 'starrail' },
  { id: 6, title: '仙舟', artist: 'HOYO-MiX', album: '星穹铁道OST', cover_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=xianzhou%20chinese%20space%20ship%20album%20cover&width=300&height=300', duration: '5:03', game: 'starrail' },
]

const fetchMusic = async () => {
  try {
    const data = await getMusic()
    music.value = data.length > 0 ? data : mockMusic
  } catch {
    music.value = mockMusic
  } finally {
    isLoading.value = false
  }
}

const togglePlay = (id: number) => {
  playingId.value = playingId.value === id ? null : id
}

onMounted(() => {
  fetchMusic()
})
</script>

<template>
  <section id="music" class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h2 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-purple-400 via-pink-400 to-red-400 bg-clip-text text-transparent">
            音乐馆
          </span>
        </h2>
        <p class="text-gray-400">聆听HOYO-MiX带来的优美旋律</p>
      </div>

      <div v-if="isLoading" class="flex justify-center py-12">
        <div class="w-12 h-12 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-4">
        <div 
          v-for="song in music" 
          :key="song.id"
          class="group relative bg-slate-800/50 backdrop-blur-sm rounded-2xl overflow-hidden border border-slate-700/50 hover:border-purple-500/50 transition-all duration-300 cursor-pointer hover:shadow-xl hover:shadow-purple-500/10 hover:-translate-y-2"
          @click="togglePlay(song.id)"
        >
          <!-- 封面图片 -->
          <div class="relative aspect-square overflow-hidden">
            <img 
              :src="song.cover_url" 
              :alt="song.title" 
              class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/30 to-transparent"></div>
            
            <!-- 播放按钮 -->
            <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
              <div class="w-14 h-14 rounded-full bg-gradient-to-r from-purple-500 to-blue-500 flex items-center justify-center shadow-lg">
                <i class="fa fa-play text-white ml-1"></i>
              </div>
            </div>
            
            <!-- 游戏标签 -->
            <span 
              class="absolute top-2 right-2 px-2 py-1 rounded-full text-xs font-medium"
              :class="song.game === 'genshin' ? 'bg-purple-500/80' : 'bg-cyan-500/80'"
            >
              {{ song.game === 'genshin' ? '原神' : '星铁' }}
            </span>
          </div>
          
          <!-- 信息区域 -->
          <div class="p-3">
            <h3 class="font-bold text-white text-sm truncate mb-1 group-hover:text-purple-300 transition-colors">
              {{ song.title }}
            </h3>
            <p class="text-gray-400 text-xs truncate mb-1">{{ song.artist }}</p>
            <div class="flex items-center justify-between">
              <span class="text-gray-500 text-xs">{{ song.album }}</span>
              <span class="text-gray-500 text-xs">{{ song.duration }}</span>
            </div>
          </div>
          
          <!-- 播放状态指示器 -->
          <div 
            v-if="playingId === song.id"
            class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-purple-500 to-blue-500 animate-pulse"
          ></div>
        </div>
      </div>
    </div>
  </section>
</template>