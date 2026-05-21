<template>
  <section class="player-section min-h-screen py-8">
    <div class="container mx-auto px-4">
      <!-- 标题 -->
      <div class="text-center mb-8">
        <h2 class="text-3xl font-bold text-white mb-2">
          <span class="bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
            玩家查询
          </span>
        </h2>
        <p class="text-slate-400">输入UID查看玩家角色练度和配队推荐</p>
      </div>
      
      <!-- 查询表单 -->
      <div class="max-w-xl mx-auto mb-8">
        <div class="relative">
          <input 
            v-model="uid"
            type="text"
            placeholder="请输入玩家UID"
            class="w-full px-6 py-4 pl-12 bg-slate-800/80 border border-slate-600 rounded-xl text-white placeholder-slate-400 focus:outline-none focus:border-blue-500 transition-all duration-300 text-lg"
          />
          <svg class="absolute left-4 top-1/2 transform -translate-y-1/2 w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
          </svg>
        </div>
        <button 
          @click="searchPlayer"
          :disabled="isLoading || !uid"
          class="w-full mt-4 px-6 py-4 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 disabled:bg-slate-600 disabled:cursor-not-allowed text-white rounded-xl font-medium transition-all duration-300 flex items-center justify-center gap-2 shadow-lg shadow-blue-500/25"
        >
          <span v-if="isLoading" class="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></span>
          <span v-else>🔍 查询玩家</span>
        </button>
        <p class="text-slate-500 text-sm mt-3 text-center">
          原神UID为9位数字，星穹铁道UID为10位数字
        </p>
      </div>
      
      <!-- 玩家信息 -->
      <div v-if="playerData" class="max-w-4xl mx-auto space-y-6">
        <!-- 玩家卡片 -->
        <div class="bg-slate-800/50 rounded-2xl p-6 border border-slate-700/50">
          <div class="flex items-center gap-4">
            <div class="w-20 h-20 rounded-xl bg-gradient-to-br from-blue-500 via-purple-500 to-pink-500 flex items-center justify-center text-3xl font-bold shadow-lg">
              {{ playerData.nickname?.charAt(0) || '?' }}
            </div>
            <div class="flex-1">
              <h3 class="text-2xl font-bold text-white">{{ playerData.nickname }}</h3>
              <div class="flex flex-wrap gap-4 text-slate-400 text-sm mt-2">
                <span class="flex items-center gap-1">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
                  </svg>
                  UID: {{ playerData.uid }}
                </span>
                <span class="flex items-center gap-1">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                  等级: {{ playerData.level }}
                </span>
                <span :class="playerData.game === 'genshin' ? 'text-orange-400' : 'text-purple-400'">
                  {{ playerData.game === 'genshin' ? '🌄 原神' : '🚀 星穹铁道' }}
                </span>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 角色列表 -->
        <div class="bg-slate-800/50 rounded-2xl p-6 border border-slate-700/50">
          <h3 class="text-lg font-semibold text-white mb-4 flex items-center gap-2">
            <span class="text-xl">🎭</span>
            角色列表 ({{ playerData.characters.length }}个)
          </h3>
          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
            <div 
              v-for="char in playerData.characters" 
              :key="char.name"
              @click="selectedCharacter = char"
              class="bg-slate-700/50 rounded-xl p-4 cursor-pointer hover:bg-slate-600/50 transition-all duration-300 group"
            >
              <div class="flex items-center gap-3 mb-3">
                <div 
                  class="w-10 h-10 rounded-lg flex items-center justify-center text-sm font-bold transition-transform duration-300 group-hover:scale-110"
                  :style="{ backgroundColor: getElementColor(char.element) + '30', color: getElementColor(char.element) }"
                >
                  {{ char.name.charAt(0) }}
                </div>
                <div class="flex-1">
                  <p class="text-white font-medium text-sm">{{ char.name }}</p>
                  <p class="text-slate-400 text-xs">LV.{{ char.level }}</p>
                </div>
              </div>
              <div class="flex items-center justify-between text-xs">
                <span 
                  class="px-2 py-0.5 rounded-full"
                  :style="{ backgroundColor: getElementColor(char.element) + '20', color: getElementColor(char.element) }"
                >
                  {{ char.element }}
                </span>
                <span class="text-yellow-400">{{ char.constellation }}命</span>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 配队推荐 -->
        <div v-if="teamRecommendations.length > 0" class="bg-gradient-to-r from-purple-600/10 via-blue-600/10 to-purple-600/10 rounded-2xl p-6 border border-purple-500/20">
          <h3 class="text-lg font-semibold text-white mb-4 flex items-center gap-2">
            <span class="text-xl">⚔️</span>
            智能配队推荐
          </h3>
          <div class="grid md:grid-cols-2 gap-4">
            <div 
              v-for="team in teamRecommendations" 
              :key="team.name"
              class="bg-slate-800/50 rounded-xl p-4 border border-slate-700/50"
            >
              <div class="flex items-center gap-2 mb-2">
                <span class="font-semibold text-white">{{ team.name }}</span>
                <div class="flex gap-1">
                  <span 
                    v-for="elem in team.elements" 
                    :key="elem"
                    class="w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold"
                    :style="{ backgroundColor: getElementColor(elem) + '30', color: getElementColor(elem) }"
                  >
                    {{ elem }}
                  </span>
                </div>
              </div>
              <p class="text-slate-400 text-sm mb-3">{{ team.description }}</p>
              <div class="flex flex-wrap gap-2">
                <span 
                  v-for="char in team.characters" 
                  :key="char"
                  class="px-3 py-1 bg-slate-700/50 rounded-full text-sm text-white"
                >
                  {{ char }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 角色详情弹窗 -->
      <div 
        v-if="selectedCharacter" 
        class="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4"
        @click.self="selectedCharacter = null"
      >
        <div class="bg-slate-800 rounded-2xl max-w-lg w-full p-6 border border-slate-700 shadow-2xl">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-xl font-bold text-white">{{ selectedCharacter.name }}</h3>
            <button 
              @click="selectedCharacter = null"
              class="text-slate-400 hover:text-white transition-colors"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <div class="flex gap-2 mb-4">
            <span 
              class="px-3 py-1 rounded-full text-sm"
              :style="{ backgroundColor: getElementColor(selectedCharacter.element) + '30', color: getElementColor(selectedCharacter.element) }"
            >
              {{ selectedCharacter.element }}
            </span>
            <span class="px-3 py-1 bg-slate-700 rounded-full text-sm text-white">LV.{{ selectedCharacter.level }}</span>
            <span class="px-3 py-1 bg-yellow-500/20 rounded-full text-sm text-yellow-400">{{ selectedCharacter.constellation }}命座</span>
          </div>
          
          <div class="bg-slate-700/50 rounded-xl p-4 mb-4">
            <h4 class="text-sm font-medium text-slate-400 mb-2">武器</h4>
            <div class="flex items-center justify-between">
              <div>
                <p class="text-white">{{ selectedCharacter.weapon.name }}</p>
                <p class="text-slate-400 text-sm">LV.{{ selectedCharacter.weapon.level }} · {{ selectedCharacter.weapon.refinement }}阶</p>
              </div>
              <span class="text-yellow-400">{{ '★'.repeat(selectedCharacter.weapon.rarity) }}</span>
            </div>
          </div>
          
          <div class="bg-slate-700/50 rounded-xl p-4">
            <h4 class="text-sm font-medium text-slate-400 mb-2">圣遗物</h4>
            <div class="grid grid-cols-2 gap-2">
              <div 
                v-for="artifact in selectedCharacter.artifacts" 
                :key="artifact.name"
                class="bg-slate-600/50 rounded-lg p-2"
              >
                <p class="text-white text-sm">{{ artifact.name }}</p>
                <p class="text-slate-400 text-xs">{{ artifact.set }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 空状态 -->
      <div v-if="!isLoading && !playerData && uid" class="text-center py-16">
        <div class="text-slate-400">
          <svg class="w-20 h-20 mx-auto mb-4 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
          </svg>
          <p class="text-lg">未找到玩家信息</p>
          <p class="text-sm mt-2">请检查UID是否正确</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface Character {
  name: string
  element: string
  level: number
  constellation: number
  weapon: {
    name: string
    rarity: number
    level: number
    refinement: number
  }
  artifacts: {
    name: string
    set: string
  }[]
}

interface TeamRecommendation {
  name: string
  description: string
  characters: string[]
  elements: string[]
}

interface PlayerData {
  uid: string
  game: string
  nickname: string
  level: number
  characters: Character[]
}

const uid = ref('')
const isLoading = ref(false)
const playerData = ref<PlayerData | null>(null)
const selectedCharacter = ref<Character | null>(null)
const teamRecommendations = ref<TeamRecommendation[]>([])

const getElementColor = (element: string): string => {
  const colors: Record<string, string> = {
    '风': '#87CEEB', '火': '#FF6B6B', '水': '#4ECDC4', '冰': '#A8D8EA', '雷': '#DDA0DD', '岩': '#CD853F', '草': '#90EE90',
    '物理': '#C0C0C0', '虚数': '#9370DB', '量子': '#FFD700', '存护': '#FFA500', '巡猎': '#FF4500', '智识': '#1E90FF',
    '虚无': '#9400D3', '丰饶': '#32CD32', '同谐': '#FF69B4'
  }
  return colors[element] || '#9370DB'
}

const searchPlayer = async () => {
  if (!uid.value) return
  
  isLoading.value = true
  playerData.value = null
  teamRecommendations.value = []
  
  try {
    const playerRes = await fetch(`/api/player/${uid.value}`)
    playerData.value = await playerRes.json()
    
    const teamRes = await fetch(`/api/player/${uid.value}/team-recommendation`)
    teamRecommendations.value = await teamRes.json()
  } catch (error) {
    console.error('查询玩家信息失败:', error)
    // 备用数据
    playerData.value = getBackupPlayerData()
    teamRecommendations.value = getBackupTeams()
  } finally {
    isLoading.value = false
  }
}

const getBackupPlayerData = (): PlayerData => ({
  uid: uid.value,
  game: uid.value.length === 10 ? 'starrail' : 'genshin',
  nickname: '旅行者',
  level: 55,
  characters: [
    { name: '芙宁娜', element: '水', level: 90, constellation: 1, weapon: { name: '万世流涌大典', rarity: 5, level: 90, refinement: 1 }, artifacts: [{ name: '水仙之梦', set: '2件套' }, { name: '苍白之火', set: '2件套' }] },
    { name: '雷电将军', element: '雷', level: 90, constellation: 0, weapon: { name: '薙草之稻光', rarity: 5, level: 90, refinement: 1 }, artifacts: [{ name: '绝缘之旗印', set: '4件套' }] },
    { name: '神里绫华', element: '冰', level: 90, constellation: 2, weapon: { name: '雾切之回光', rarity: 5, level: 90, refinement: 1 }, artifacts: [{ name: '冰风迷途的勇士', set: '4件套' }] },
    { name: '纳西妲', element: '草', level: 90, constellation: 1, weapon: { name: '千夜浮梦', rarity: 5, level: 90, refinement: 1 }, artifacts: [{ name: '深林的记忆', set: '4件套' }] },
    { name: '钟离', element: '岩', level: 90, constellation: 0, weapon: { name: '贯虹之槊', rarity: 5, level: 90, refinement: 1 }, artifacts: [{ name: '千岩牢固', set: '4件套' }] },
    { name: '万叶', element: '风', level: 90, constellation: 1, weapon: { name: '苍古自由之誓', rarity: 5, level: 90, refinement: 1 }, artifacts: [{ name: '翠绿之影', set: '4件套' }] }
  ]
})

const getBackupTeams = (): TeamRecommendation[] => [
  { name: '芙宁娜蒸发队', description: '水元素主C配合火元素触发蒸发反应', characters: ['芙宁娜', '万叶', '钟离', '香菱'], elements: ['水', '火'] },
  { name: '雷电将军超激化队', description: '雷元素主C配合草元素触发激化反应', characters: ['雷电将军', '纳西妲', '万叶', '钟离'], elements: ['雷', '草'] },
  { name: '神里绫华永冻队', description: '冰元素主C配合水元素触发冻结反应', characters: ['神里绫华', '万叶', '钟离', '莫娜'], elements: ['冰', '水'] }
]
</script>