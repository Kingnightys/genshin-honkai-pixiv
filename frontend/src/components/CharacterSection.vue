<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Character {
  id: number
  name: string
  element: string
  rarity: number
  avatar: string
}

const activeTab = ref('genshin')
const genshinCharacters = ref<Character[]>([])
const starrailCharacters = ref<Character[]>([])
const isLoading = ref(true)

// Mock数据
const mockGenshin: Character[] = [
  { id: 1, name: '钟离', element: '岩', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=zhongli%20portrait%20anime&width=128&height=128' },
  { id: 2, name: '雷电将军', element: '雷', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=raiden%20shogun%20portrait%20anime&width=128&height=128' },
  { id: 3, name: '神里绫华', element: '冰', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=ayaka%20portrait%20anime&width=128&height=128' },
  { id: 4, name: '纳西妲', element: '草', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=nahida%20portrait%20anime&width=128&height=128' },
  { id: 5, name: '枫原万叶', element: '风', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=kazuha%20portrait%20anime&width=128&height=128' },
  { id: 6, name: '胡桃', element: '火', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=hutao%20portrait%20anime&width=128&height=128' },
]

const mockStarrail: Character[] = [
  { id: 1, name: '开拓者', element: '物理', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=trailblazer%20honkai%20portrait&width=128&height=128' },
  { id: 2, name: '希儿', element: '量子', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=seele%20honkai%20portrait&width=128&height=128' },
  { id: 3, name: '景元', element: '雷', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=jing%20yuan%20honkai%20portrait&width=128&height=128' },
  { id: 4, name: '布洛妮娅', element: '风', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=bronya%20honkai%20portrait&width=128&height=128' },
  { id: 5, name: '银狼', element: '量子', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=sliver%20wolf%20honkai%20portrait&width=128&height=128' },
  { id: 6, name: '罗刹', element: '虚数', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=luka%20honkai%20portrait&width=128&height=128' },
]

const fetchCharacters = async () => {
  try {
    const [genshinRes, starrailRes] = await Promise.all([
      axios.get('http://192.168.8.49:8000/api/characters/genshin'),
      axios.get('http://192.168.8.49:8000/api/characters/starrail')
    ])
    genshinCharacters.value = genshinRes.data.data || mockGenshin
    starrailCharacters.value = starrailRes.data.data || mockStarrail
  } catch {
    genshinCharacters.value = mockGenshin
    starrailCharacters.value = mockStarrail
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchCharacters()
})
</script>

<template>
  <section id="characters" class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-4xl font-bold text-center mb-8">角色展览馆</h2>
      
      <div class="flex justify-center gap-4 mb-8">
        <button 
          class="px-6 py-3 rounded-xl font-bold transition-all"
          :class="activeTab === 'genshin' ? 'bg-gradient-to-r from-purple-500 to-blue-500' : 'bg-slate-800 hover:bg-slate-700'"
          @click="activeTab = 'genshin'"
        >
          原神
        </button>
        <button 
          class="px-6 py-3 rounded-xl font-bold transition-all"
          :class="activeTab === 'starrail' ? 'bg-gradient-to-r from-purple-500 to-blue-500' : 'bg-slate-800 hover:bg-slate-700'"
          @click="activeTab = 'starrail'"
        >
          星穹铁道
        </button>
      </div>

      <div v-if="isLoading" class="flex justify-center">
        <div class="w-10 h-10 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
        <div 
          v-for="char in (activeTab === 'genshin' ? genshinCharacters : starrailCharacters)" 
          :key="char.id"
          class="bg-slate-800/50 rounded-xl p-4 text-center hover:scale-105 transition-transform cursor-pointer"
        >
          <img :src="char.avatar" :alt="char.name" class="w-20 h-20 rounded-full mx-auto mb-2 border-2 border-slate-600" />
          <h4 class="font-bold">{{ char.name }}</h4>
          <p class="text-sm text-gray-400">{{ char.element }}</p>
          <div class="flex justify-center gap-0.5 mt-1">
            <i v-for="i in char.rarity" :key="i" class="fa fa-star text-yellow-400 text-sm"></i>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
