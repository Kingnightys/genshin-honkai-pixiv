<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import CharacterCard from './CharacterCard.vue'
import { getCharacters } from '@/api'
import type { Character } from '@/types'

interface Game {
  id: 'genshin' | 'starrail';
  name: string;
  icon: string;
  gradient: string;
}

const games: Game[] = [
  { id: 'genshin', name: '原神', icon: '🌄', gradient: 'linear-gradient(to right, #f97316, #ef4444)' },
  { id: 'starrail', name: '星穹铁道', icon: '🚀', gradient: 'linear-gradient(to right, #8b5cf6, #3b82f6)' }
]

// 默认数据
const defaultGenshinCharacters: Character[] = [
  { id: 1, name: '旅行者', name_en: 'Traveler', game: 'genshin', version: '1.0', element: '风', element_en: 'Anemo', rarity: 5, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20traveler%20anemo%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20traveler%20anemo%20character%20portrait&width=256&height=256', created_at: Date.now() },
  { id: 2, name: '安柏', name_en: 'Amber', game: 'genshin', version: '1.0', element: '火', element_en: 'Pyro', rarity: 4, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20amber%20pyro%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20amber%20pyro%20character%20portrait&width=256&height=256', created_at: Date.now() },
  { id: 3, name: '丽莎', name_en: 'Lisa', game: 'genshin', version: '1.0', element: '雷', element_en: 'Electro', rarity: 4, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20lisa%20electro%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20lisa%20electro%20character%20portrait&width=256&height=256', created_at: Date.now() },
  { id: 4, name: '凯亚', name_en: 'Kaeya', game: 'genshin', version: '1.0', element: '冰', element_en: 'Cryo', rarity: 4, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20kaeya%20cryo%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20kaeya%20cryo%20character%20portrait&width=256&height=256', created_at: Date.now() },
  { id: 5, name: '芭芭拉', name_en: 'Barbara', game: 'genshin', version: '1.0', element: '水', element_en: 'Hydro', rarity: 4, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20barbara%20hydro%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20barbara%20hydro%20character%20portrait&width=256&height=256', created_at: Date.now() },
  { id: 6, name: '迪卢克', name_en: 'Diluc', game: 'genshin', version: '1.0', element: '火', element_en: 'Pyro', rarity: 5, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20diluc%20pyro%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20impact%20diluc%20pyro%20character%20portrait&width=256&height=256', created_at: Date.now() },
]

const defaultStarrailCharacters: Character[] = [
  { id: 101, name: '开拓者', name_en: 'Trailblazer', game: 'starrail', version: '1.0', element: '物理', element_en: 'Physical', rarity: 5, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20trailblazer%20physical%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20trailblazer%20physical%20character%20portrait&width=256&height=256', created_at: Date.now() },
  { id: 102, name: '三月七', name_en: 'March 7th', game: 'starrail', version: '1.0', element: '冰', element_en: 'Cryo', rarity: 4, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20march%207th%20cryo%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20march%207th%20cryo%20character%20portrait&width=256&height=256', created_at: Date.now() },
  { id: 103, name: '丹恒', name_en: 'Dan Heng', game: 'starrail', version: '1.0', element: '风', element_en: 'Anemo', rarity: 4, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20dan%20heng%20wind%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20dan%20heng%20wind%20character%20portrait&width=256&height=256', created_at: Date.now() },
  { id: 104, name: '姬子', name_en: 'Himeko', game: 'starrail', version: '1.0', element: '火', element_en: 'Fire', rarity: 5, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20himeko%20fire%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20himeko%20fire%20character%20portrait&width=256&height=256', created_at: Date.now() },
  { id: 105, name: '瓦尔特', name_en: 'Welt', game: 'starrail', version: '1.0', element: '虚数', element_en: 'Imaginary', rarity: 5, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20welt%20imaginary%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20welt%20imaginary%20character%20portrait&width=256&height=256', created_at: Date.now() },
  { id: 106, name: '布洛妮娅', name_en: 'Bronya', game: 'starrail', version: '1.1', element: '风', element_en: 'Wind', rarity: 5, image_url: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20bronya%20wind%20character%20portrait&width=256&height=256', local_path: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20bronya%20wind%20character%20portrait&width=256&height=256', created_at: Date.now() },
]

const currentGame = ref<'genshin' | 'starrail'>('genshin')
const searchQuery = ref('')
const rarityFilter = ref('')
const isLoading = ref(true)
const selectedCharacter = ref<Character | null>(null)
const genshinCharacters = ref<Character[]>([])
const starrailCharacters = ref<Character[]>([])

const currentCharacters = computed(() => {
  return currentGame.value === 'genshin' ? genshinCharacters.value : starrailCharacters.value
})

const filteredCharacters = computed(() => {
  let result = currentCharacters.value
  
  // 搜索过滤
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(char => 
      char.name.toLowerCase().includes(query) ||
      char.element.toLowerCase().includes(query)
    )
  }
  
  // 稀有度过滤
  if (rarityFilter.value) {
    result = result.filter(char => char.rarity === parseInt(rarityFilter.value))
  }
  
  return result
})

const fetchCharacters = async () => {
  isLoading.value = true
  try {
    const genshinRes = await getCharacters('genshin')
    const starrailRes = await getCharacters('starrail')
    
    genshinCharacters.value = genshinRes.length > 0 ? genshinRes : defaultGenshinCharacters
    starrailCharacters.value = starrailRes.length > 0 ? starrailRes : defaultStarrailCharacters
  } catch (error) {
    console.error('获取角色数据失败:', error)
    // 使用默认数据
    genshinCharacters.value = defaultGenshinCharacters
    starrailCharacters.value = defaultStarrailCharacters
  } finally {
    isLoading.value = false
  }
}

const handleSelect = (character: Character) => {
  selectedCharacter.value = character
}

const getElementColor = (element: string): string => {
  const colors: Record<string, string> = {
    '风': '#87CEEB', '火': '#FF6B6B', '水': '#4ECDC4', '冰': '#A8D8EA', '雷': '#DDA0DD', '岩': '#CD853F', '草': '#90EE90',
    '物理': '#C0C0C0', '虚数': '#9370DB', '量子': '#FFD700', '存护': '#FFA500', '巡猎': '#FF4500', '智识': '#1E90FF',
    '虚无': '#9400D3', '丰饶': '#32CD32', '同谐': '#FF69B4'
  }
  return colors[element] || '#9370DB'
}

onMounted(() => {
  fetchCharacters()
})
</script>

<template>
  <div class="characters-list">
    <!-- 游戏切换和搜索 -->
    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-8">
      <!-- 游戏切换 -->
      <div class="flex gap-3">
        <button 
          v-for="game in games" 
          :key="game.id"
          @click="currentGame = game.id"
          class="px-5 py-2 rounded-full font-medium transition-all duration-300 flex items-center gap-2"
          :class="currentGame === game.id 
            ? 'text-white shadow-lg' 
            : 'bg-slate-700/50 text-slate-400 hover:bg-slate-600/50'"
          :style="currentGame === game.id ? { background: game.gradient } : {}"
        >
          <span class="text-lg">{{ game.icon }}</span>
          {{ game.name }}
        </button>
      </div>
      
      <!-- 搜索和筛选 -->
      <div class="flex items-center gap-3">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="搜索角色..."
          class="px-4 py-2 bg-slate-800/50 border border-slate-600 rounded-full text-white text-sm focus:outline-none focus:border-purple-500 transition-colors w-48"
        />
        <select 
          v-model="rarityFilter"
          class="px-4 py-2 bg-slate-800/50 border border-slate-600 rounded-full text-white text-sm focus:outline-none focus:border-purple-500 transition-colors"
        >
          <option value="">全部稀有度</option>
          <option value="4">★★★★</option>
          <option value="5">★★★★★</option>
        </select>
      </div>
    </div>
    
    <!-- 角色网格 -->
    <div v-if="!isLoading" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4 sm:gap-6">
      <CharacterCard 
        v-for="char in filteredCharacters" 
        :key="char.id" 
        :character="{ ...char, local_path: char.local_path ?? '' }"
        @select="(c: any) => handleSelect(c)"
      />
    </div>
    
    <!-- 加载状态 -->
    <div v-if="isLoading" class="flex justify-center items-center py-12">
      <div class="animate-spin rounded-full h-10 w-10 border-b-2 border-purple-500"></div>
    </div>
    
    <!-- 空状态 -->
    <div v-if="!isLoading && filteredCharacters.length === 0" class="text-center py-12">
      <div class="text-slate-400">
        <svg class="w-16 h-16 mx-auto mb-4 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <p>没有找到匹配的角色</p>
      </div>
    </div>
    
    <!-- 角色详情弹窗 -->
    <Teleport to="body">
      <div 
        v-if="selectedCharacter"
        class="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4"
        @click.self="selectedCharacter = null"
      >
        <div class="bg-slate-800 rounded-2xl max-w-md w-full p-6 border border-slate-700 shadow-2xl">
          <div class="flex gap-4">
            <img 
              :src="selectedCharacter.image_url" 
              :alt="selectedCharacter.name"
              class="w-24 h-24 rounded-xl object-cover border-2 border-purple-500/50"
            />
            <div class="flex-1">
              <h3 class="text-2xl font-bold text-white">{{ selectedCharacter.name }}</h3>
              <div class="flex gap-2 mt-2">
                <span 
                  class="px-2 py-1 rounded-full text-sm"
                  :style="{ backgroundColor: getElementColor(selectedCharacter.element) + '30', color: getElementColor(selectedCharacter.element) }"
                >
                  {{ selectedCharacter.element }}
                </span>
                <span class="text-yellow-400">
                  {{ '★'.repeat(selectedCharacter.rarity) }}
                </span>
              </div>
              <p class="text-slate-400 text-sm mt-2">版本 {{ selectedCharacter.version }}</p>
            </div>
          </div>
          <p class="text-slate-300 mt-4">{{ selectedCharacter.description || '暂无描述信息' }}</p>
          <button 
            @click="selectedCharacter = null"
            class="mt-6 w-full py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-full transition-colors"
          >
            关闭
          </button>
        </div>
      </div>
    </Teleport>
  </div>
</template>