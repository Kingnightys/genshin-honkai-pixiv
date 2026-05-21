<!-- src/views/CharactersView.vue -->
<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { getCharacters } from '@/api'
import type { Character } from '@/types'
import CharacterCard from '@/components/CharacterCard.vue'

const game = ref<'genshin' | 'starrail'>('genshin')
const characters = ref<Character[]>([])
const isLoading = ref(true)
const activeElement = ref('全部')
const selectedCharacter = ref<Character | null>(null)

// 原神元素
const genshinElements = ['全部', '火', '水', '风', '雷', '岩', '草', '冰']
// 星穹铁道命途
const starrailElements = ['全部', '物理', '火', '冰', '雷', '风', '量子', '虚数', '巡猎', '智识', '同谐', '毁灭', '存护', '丰饶']

const currentElements = computed(() => 
  game.value === 'genshin' ? genshinElements : starrailElements
)

const filteredCharacters = computed(() => {
  if (activeElement.value === '全部') return characters.value
  return characters.value.filter(c => c.element === activeElement.value)
})

const fetchCharacters = async () => {
  isLoading.value = true
  characters.value = await getCharacters(game.value)
  isLoading.value = false
}

const filterByElement = (element: string) => {
  activeElement.value = element
}

const openCharacterDetail = (character: Character) => {
  selectedCharacter.value = character
}

const closeCharacterDetail = () => {
  selectedCharacter.value = null
}

onMounted(() => {
  fetchCharacters()
})
</script>

<template>
  <div class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题区域 -->
      <div class="text-center mb-12">
        <div class="inline-flex items-center gap-2 px-4 py-2 mb-6 rounded-full backdrop-blur-sm" 
          :class="game === 'genshin' ? 'bg-purple-500/20 border border-purple-500/30' : 'bg-cyan-500/20 border border-cyan-500/30'">
          <i :class="game === 'genshin' ? 'fa fa-sun text-yellow-400' : 'fa fa-star text-cyan-400'"></i>
          <span class="text-sm" :class="game === 'genshin' ? 'text-purple-300' : 'text-cyan-300'">
            {{ game === 'genshin' ? '提瓦特大陆' : '星际世界' }}
          </span>
        </div>
        <h1 class="text-4xl lg:text-5xl font-bold mb-4">
          <span :class="game === 'genshin' ? 'text-genshin-gradient' : 'text-starrail-gradient'">
            角色图鉴
          </span>
        </h1>
        <p class="text-gray-400 max-w-2xl mx-auto">
          {{ game === 'genshin' ? '探索提瓦特大陆的七元素英雄' : '探索星际世界的命途行者' }}
        </p>
      </div>

      <!-- 游戏切换 -->
      <div class="flex justify-center gap-4 mb-8">
        <button
          class="px-8 py-3 rounded-xl font-bold transition-all duration-300 flex items-center gap-3 shadow-lg"
          :class="game === 'genshin' 
            ? 'bg-gradient-to-r from-purple-500 via-pink-500 to-blue-500 text-white shadow-purple-500/30 hover:shadow-purple-500/50' 
            : 'bg-slate-800/80 hover:bg-slate-700 border border-slate-600 hover:border-purple-500/50'"
          @click="game = 'genshin'; activeElement = '全部'; fetchCharacters()"
        >
          <i class="fa fa-sun text-lg"></i>
          <span>原神</span>
          <span class="text-xs px-2 py-0.5 rounded-full bg-white/20">提瓦特</span>
        </button>
        <button
          class="px-8 py-3 rounded-xl font-bold transition-all duration-300 flex items-center gap-3 shadow-lg"
          :class="game === 'starrail' 
            ? 'bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-500 text-white shadow-cyan-500/30 hover:shadow-cyan-500/50' 
            : 'bg-slate-800/80 hover:bg-slate-700 border border-slate-600 hover:border-cyan-500/50'"
          @click="game = 'starrail'; activeElement = '全部'; fetchCharacters()"
        >
          <i class="fa fa-star text-lg"></i>
          <span>星穹铁道</span>
          <span class="text-xs px-2 py-0.5 rounded-full bg-white/20">星际</span>
        </button>
      </div>

      <!-- 元素/命途筛选 -->
      <div class="flex flex-wrap justify-center gap-2 mb-10">
        <button
          v-for="element in currentElements"
          :key="element"
          class="px-5 py-2.5 rounded-full font-medium transition-all duration-300 backdrop-blur-sm border"
          :class="activeElement === element 
            ? (game === 'genshin' 
                ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white border-purple-500/50' 
                : 'bg-gradient-to-r from-cyan-500 to-blue-500 text-white border-cyan-500/50')
            : 'bg-white/5 hover:bg-white/15 border-white/10 hover:border-white/20'"
          @click="filterByElement(element)"
        >
          {{ element }}
        </button>
      </div>

      <!-- 角色列表 -->
      <div v-if="isLoading" class="flex justify-center items-center py-20">
        <div class="relative">
          <div class="w-16 h-16 border-4 rounded-full animate-spin" 
            :class="game === 'genshin' ? 'border-purple-500 border-t-transparent' : 'border-cyan-500 border-t-transparent'"></div>
          <div class="absolute inset-0 flex items-center justify-center">
            <i :class="game === 'genshin' ? 'fa fa-sun text-purple-400' : 'fa fa-star text-cyan-400'"></i>
          </div>
        </div>
      </div>

      <div v-else class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4 lg:gap-6">
        <CharacterCard
          v-for="character in filteredCharacters"
          :key="character.id"
          :character="{ ...character, local_path: character.local_path ?? '' }"
          @click="openCharacterDetail(character)"
        />
      </div>

      <div v-if="!isLoading && filteredCharacters.length === 0" class="text-center py-20">
        <div class="w-20 h-20 mx-auto mb-4 rounded-full bg-white/5 flex items-center justify-center">
          <i :class="game === 'genshin' ? 'fa fa-sun text-4xl text-purple-400' : 'fa fa-star text-4xl text-cyan-400'"></i>
        </div>
        <p class="text-gray-400">暂无该属性角色</p>
      </div>
    </div>

    <!-- 角色详情弹窗 -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selectedCharacter" class="fixed inset-0 z-50 flex items-center justify-center p-4" @click.self="closeCharacterDetail">
          <!-- 背景遮罩 -->
          <div class="absolute inset-0 bg-slate-900/95 backdrop-blur-xl"></div>
          
          <!-- 弹窗内容 -->
          <div class="relative w-full max-w-2xl bg-slate-800/90 backdrop-blur-xl rounded-3xl border border-white/10 overflow-hidden shadow-2xl">
            <!-- 背景图 -->
            <div class="relative h-48 overflow-hidden">
              <img :src="selectedCharacter.image_url || selectedCharacter.image" :alt="selectedCharacter.name"
                class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-800 via-slate-800/50 to-transparent"></div>
              
              <!-- 关闭按钮 -->
              <button @click="closeCharacterDetail" class="absolute top-4 right-4 p-2 rounded-full bg-white/10 hover:bg-white/20 transition-colors">
                <i class="fa fa-times text-white"></i>
              </button>
            </div>
            
            <!-- 角色信息 -->
            <div class="relative px-6 pb-6" style="margin-top: -60px;">
              <!-- 头像 -->
              <div class="relative w-28 h-28 mx-auto mb-4">
                <img :src="selectedCharacter.image_url || selectedCharacter.image" :alt="selectedCharacter.name"
                  class="w-full h-full rounded-full object-cover border-4 border-slate-800" />
                <div class="absolute inset-0 rounded-full border-2" 
                  :class="selectedCharacter.game === 'genshin' ? 'border-purple-500/50' : 'border-cyan-500/50'"></div>
              </div>
              
              <!-- 名称和稀有度 -->
              <div class="text-center mb-6">
                <h2 class="text-3xl font-bold mb-2" :class="selectedCharacter.game === 'genshin' ? 'text-genshin-gradient' : 'text-starrail-gradient'">
                  {{ selectedCharacter.name }}
                </h2>
                <div class="flex justify-center gap-1">
                  <i v-for="i in selectedCharacter.rarity" :key="i" 
                    class="fa fa-star text-yellow-400" :class="i <= 4 ? 'text-lg' : 'text-xl'"></i>
                </div>
              </div>
              
              <!-- 属性信息 -->
              <div class="grid grid-cols-3 gap-4 mb-6">
                <div class="bg-white/5 rounded-xl p-4 text-center">
                  <div class="text-xs text-gray-400 mb-1">元素/命途</div>
                  <div class="font-bold" :class="selectedCharacter.game === 'genshin' ? 'text-purple-400' : 'text-cyan-400'">
                    {{ selectedCharacter.element }}
                  </div>
                </div>
                <div class="bg-white/5 rounded-xl p-4 text-center">
                  <div class="text-xs text-gray-400 mb-1">武器/属性</div>
                  <div class="font-bold text-white">
                    {{ (selectedCharacter as any).weapon || (selectedCharacter as any).path || '-' }}
                  </div>
                </div>
                <div class="bg-white/5 rounded-xl p-4 text-center">
                  <div class="text-xs text-gray-400 mb-1">地区/阵营</div>
                  <div class="font-bold text-white">
                    {{ selectedCharacter.region || '-' }}
                  </div>
                </div>
              </div>
              
              <!-- 描述 -->
              <div class="bg-white/5 rounded-xl p-4">
                <div class="text-xs text-gray-400 mb-2">角色简介</div>
                <p class="text-gray-300 text-sm leading-relaxed">
                  {{ selectedCharacter.description || `「${selectedCharacter.name}」是一位强大的${selectedCharacter.element}属性角色。` }}
                </p>
              </div>
              
              <!-- 版本信息 -->
              <div class="mt-4 text-center text-xs text-gray-500">
                登场版本：{{ selectedCharacter.version || '未知' }}
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: all 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from > div:last-child,
.modal-leave-to > div:last-child {
  transform: scale(0.9) translateY(20px);
}
</style>