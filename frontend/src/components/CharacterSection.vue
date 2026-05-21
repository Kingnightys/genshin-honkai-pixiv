<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getCharacters } from '@/api'

interface LocalCharacter {
  id: number
  name: string
  element: string
  rarity: number
  avatar: string
}

const activeTab = ref<'genshin' | 'starrail'>('genshin')
const genshinCharacters = ref<LocalCharacter[]>([])
const starrailCharacters = ref<LocalCharacter[]>([])
const isLoading = ref(true)

// Mock数据
const mockGenshin: LocalCharacter[] = [
  { id: 1, name: '钟离', element: '岩', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=zhongli%20genshin%20portrait%20anime%20style&width=256&height=256' },
  { id: 2, name: '雷电将军', element: '雷', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=raiden%20shogun%20genshin%20portrait%20anime&width=256&height=256' },
  { id: 3, name: '神里绫华', element: '冰', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=ayaka%20genshin%20portrait%20anime&width=256&height=256' },
  { id: 4, name: '纳西妲', element: '草', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=nahida%20genshin%20portrait%20anime&width=256&height=256' },
  { id: 5, name: '枫原万叶', element: '风', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=kazuha%20genshin%20portrait%20anime&width=256&height=256' },
  { id: 6, name: '胡桃', element: '火', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=hutao%20genshin%20portrait%20anime&width=256&height=256' },
]

const mockStarrail: LocalCharacter[] = [
  { id: 1, name: '开拓者', element: '物理', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=trailblazer%20honkai%20star%20rail%20portrait&width=256&height=256' },
  { id: 2, name: '希儿', element: '量子', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=seele%20honkai%20star%20rail%20portrait&width=256&height=256' },
  { id: 3, name: '景元', element: '雷', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=jing%20yuan%20honkai%20star%20rail%20portrait&width=256&height=256' },
  { id: 4, name: '布洛妮娅', element: '风', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=bronya%20honkai%20star%20rail%20portrait&width=256&height=256' },
  { id: 5, name: '银狼', element: '量子', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=sliver%20wolf%20honkai%20star%20rail%20portrait&width=256&height=256' },
  { id: 6, name: '罗刹', element: '虚数', rarity: 5, avatar: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=luocha%20honkai%20star%20rail%20portrait&width=256&height=256' },
]

const getElementColor = (element: string): string => {
  const colors: Record<string, string> = {
    '火': 'from-red-500 to-orange-500',
    '水': 'from-blue-500 to-cyan-500',
    '风': 'from-green-500 to-emerald-500',
    '雷': 'from-purple-500 to-pink-500',
    '岩': 'from-amber-500 to-yellow-500',
    '草': 'from-lime-500 to-green-500',
    '冰': 'from-cyan-500 to-blue-400',
    '物理': 'from-gray-400 to-gray-500',
    '虚无': 'from-purple-600 to-purple-400',
    '巡猎': 'from-orange-500 to-red-500',
    '智识': 'from-blue-500 to-cyan-500',
    '同谐': 'from-green-400 to-emerald-500',
    '毁灭': 'from-red-600 to-orange-500',
    '存护': 'from-yellow-500 to-amber-500',
    '丰饶': 'from-pink-400 to-rose-500'
  }
  return colors[element] || 'from-gray-500 to-gray-600'
}

const ensureAvatar = (c: any): LocalCharacter => {
  return {
    id: c.id,
    name: c.name,
    element: c.element,
    rarity: c.rarity,
    avatar:
      c.avatar ??
      `https://neeko-copilot.bytedance.net/api/text2image?prompt=${encodeURIComponent(c.name || 'character')}%20portrait%20anime&width=256&height=256`,
  }
}

const fetchCharacters = async () => {
  try {
    const genshinData = await getCharacters('genshin')
    const starrailData = await getCharacters('starrail')
    genshinCharacters.value = genshinData && genshinData.length > 0 ? genshinData.map(ensureAvatar) : mockGenshin
    starrailCharacters.value = starrailData && starrailData.length > 0 ? starrailData.map(ensureAvatar) : mockStarrail
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
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h2 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-purple-400 via-pink-400 to-blue-400 bg-clip-text text-transparent">
            角色展览馆
          </span>
        </h2>
        <p class="text-gray-400">探索提瓦特与星际世界的英雄们</p>
      </div>
      
      <!-- 游戏切换 -->
      <div class="flex justify-center gap-4 mb-10">
        <button 
          class="px-8 py-3 rounded-xl font-bold transition-all duration-300 flex items-center gap-2"
          :class="activeTab === 'genshin' ? 'bg-gradient-to-r from-purple-500 via-pink-500 to-blue-500 shadow-lg shadow-purple-500/30' : 'bg-slate-800/80 hover:bg-slate-700 border border-slate-600'"
          @click="activeTab = 'genshin'"
        >
          <i class="fa fa-sun"></i>
          原神
        </button>
        <button 
          class="px-8 py-3 rounded-xl font-bold transition-all duration-300 flex items-center gap-2"
          :class="activeTab === 'starrail' ? 'bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-500 shadow-lg shadow-cyan-500/30' : 'bg-slate-800/80 hover:bg-slate-700 border border-slate-600'"
          @click="activeTab = 'starrail'"
        >
          <i class="fa fa-star"></i>
          星穹铁道
        </button>
      </div>

      <div v-if="isLoading" class="flex justify-center py-12">
        <div class="w-12 h-12 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4">
        <div 
          v-for="char in (activeTab === 'genshin' ? genshinCharacters : starrailCharacters)" 
          :key="char.id"
          class="group relative bg-slate-800/50 backdrop-blur-sm rounded-2xl p-4 text-center border border-slate-700/50 hover:border-white/30 transition-all duration-300 cursor-pointer hover:shadow-xl hover:shadow-purple-500/10 hover:-translate-y-2"
        >
          <!-- 角色头像 -->
          <div class="relative w-20 h-20 mx-auto mb-3">
            <img 
              :src="char.avatar" 
              :alt="char.name" 
              class="w-full h-full rounded-full object-cover border-3 transition-all duration-300"
              :class="`border-gradient-to-br ${getElementColor(char.element)}`"
            />
            <!-- 悬浮光效 -->
            <div class="absolute inset-0 rounded-full bg-gradient-to-br opacity-0 group-hover:opacity-50 transition-opacity" :class="getElementColor(char.element)"></div>
          </div>
          
          <!-- 角色名称 -->
          <h4 class="font-bold text-white mb-1 group-hover:text-purple-300 transition-colors">
            {{ char.name }}
          </h4>
          
          <!-- 元素属性 -->
          <span class="inline-block px-2 py-1 rounded-full text-xs font-medium mb-2" :class="`bg-gradient-to-r ${getElementColor(char.element)}`">
            {{ char.element }}
          </span>
          
          <!-- 稀有度 -->
          <div class="flex justify-center gap-1">
            <i 
              v-for="i in char.rarity" 
              :key="i" 
              class="fa fa-star text-yellow-400" 
              :class="i <= 4 ? 'text-sm' : 'text-base'"
            ></i>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>