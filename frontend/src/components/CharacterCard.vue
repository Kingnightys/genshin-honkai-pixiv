<!-- d:\AiCodeProject\genshin-honkai-pixiv\frontend\src\components\CharacterCard.vue -->
<script setup lang="ts">
import { computed } from 'vue'
import type { Character } from '@/types'

const props = defineProps<{
  character: Character
}>()

const emit = defineEmits<{
  click: [character: Character]
}>()

// computed fallback to support cases where `path` may not exist on Character
const displayWeapon = computed(() => {
  return (props.character as any).weapon || (props.character as any).path || ''
})

const getElementColor = (element: string) => {
  const colors: Record<string, string> = {
    // 原神元素
    '火': 'from-red-500 to-orange-500',
    '水': 'from-blue-500 to-cyan-500',
    '风': 'from-green-500 to-emerald-500',
    '雷': 'from-purple-500 to-pink-500',
    '岩': 'from-amber-500 to-yellow-500',
    '草': 'from-lime-500 to-green-500',
    '冰': 'from-cyan-500 to-blue-400',
    // 星穹铁道命途
    '物理': 'from-gray-400 to-gray-500',
    '虚数': 'from-purple-600 to-indigo-400',
    '量子': 'from-violet-500 to-purple-400',
    '巡猎': 'from-orange-500 to-red-500',
    '智识': 'from-blue-500 to-cyan-500',
    '同谐': 'from-green-400 to-emerald-500',
    '毁灭': 'from-red-600 to-orange-500',
    '存护': 'from-yellow-500 to-amber-500',
    '丰饶': 'from-pink-400 to-rose-500'
  }
  return colors[element] || 'from-gray-500 to-gray-600'
}

const getElementGlow = (element: string) => {
  const glows: Record<string, string> = {
    '火': 'shadow-red-500/30',
    '水': 'shadow-blue-500/30',
    '风': 'shadow-green-500/30',
    '雷': 'shadow-purple-500/30',
    '岩': 'shadow-amber-500/30',
    '草': 'shadow-lime-500/30',
    '冰': 'shadow-cyan-500/30',
    '物理': 'shadow-gray-500/30',
    '虚数': 'shadow-purple-500/30',
    '量子': 'shadow-violet-500/30',
    '巡猎': 'shadow-orange-500/30',
    '智识': 'shadow-blue-500/30',
    '同谐': 'shadow-green-500/30',
    '毁灭': 'shadow-red-500/30',
    '存护': 'shadow-yellow-500/30',
    '丰饶': 'shadow-pink-500/30'
  }
  return glows[element] || 'shadow-gray-500/30'
}

const getRarityStars = (rarity: number) => {
  return Array(rarity).fill(0)
}

const handleClick = () => {
  emit('click', props.character)
}
</script>

<template>
  <div
    class="group relative bg-white/5 backdrop-blur-md rounded-2xl overflow-hidden border border-white/10 hover:border-white/30 transition-all duration-500 card-hover cursor-pointer"
    @click="handleClick">
    
    <!-- 动态背景光效 -->
    <div 
      :class="`absolute inset-0 bg-gradient-to-br ${getElementColor(character.element)} opacity-0 group-hover:opacity-8 transition-opacity duration-500`">
    </div>
    
    <!-- 角色图片 -->
    <div class="relative aspect-square overflow-hidden">
      <img :src="character.image_url || character.image" :alt="character.name"
        class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" />
      <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent"></div>

      <!-- 元素标签 -->
      <div
        :class="`absolute top-2 right-2 px-2.5 py-1.5 rounded-full text-xs font-bold bg-gradient-to-r ${getElementColor(character.element)} backdrop-blur-md shadow-lg ${getElementGlow(character.element)}`">
        <span class="flex items-center gap-1">{{ character.element }}</span>
      </div>

      <!-- 游戏标识 -->
      <div 
        class="absolute top-2 left-2 px-2.5 py-1.5 rounded-full text-xs font-bold backdrop-blur-md"
        :class="character.game === 'genshin' ? 'bg-purple-500/80 text-purple-100' : 'bg-cyan-500/80 text-cyan-100'">
        <span class="flex items-center gap-1">
          <i :class="character.game === 'genshin' ? 'fa fa-sun' : 'fa fa-star'"></i>
          {{ character.game === 'genshin' ? '原神' : '星穹' }}
        </span>
      </div>
      
      <!-- 悬浮时的光晕效果 -->
      <div 
        :class="`absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 bg-gradient-to-br ${getElementColor(character.element)} blur-xl`">
      </div>
    </div>

    <!-- 角色信息 -->
    <div class="p-3 lg:p-4 relative">
      <!-- 角色名称 -->
      <div class="flex items-center justify-between mb-2">
        <h3 class="font-bold text-white text-sm lg:text-base truncate group-hover:text-purple-300 transition-colors">
          {{ character.name }}
        </h3>
        <div class="flex items-center gap-0.5">
          <i 
            v-for="(_, index) in getRarityStars(character.rarity)" 
            :key="index" 
            class="fa fa-star transition-all duration-300" 
            :class="index < 4 ? 'text-yellow-400 text-xs' : 'text-yellow-300 text-sm group-hover:scale-125'"
          ></i>
        </div>
      </div>

      <!-- 属性信息 -->
      <div class="flex items-center justify-between text-xs text-gray-400">
        <span class="truncate max-w-[60px] group-hover:text-white transition-colors">{{ displayWeapon || '未知' }}</span>
        <span class="truncate max-w-[60px] group-hover:text-white transition-colors">{{ character.region || '未知' }}</span>
      </div>

      <!-- 版本信息 -->
      <div class="mt-2 pt-2 border-t border-white/10">
        <span class="text-xs text-gray-500">
          <i class="fa fa-tag mr-1"></i>版本 {{ character.version || '未知' }}
        </span>
      </div>
    </div>

    <!-- 悬浮边框光效 -->
    <div
      :class="`absolute inset-0 rounded-2xl border-2 opacity-0 group-hover:opacity-60 transition-all duration-300 shadow-lg ${getElementGlow(character.element)}`"
      :style="{ borderImage: `linear-gradient(135deg, ${getElementColor(character.element).replace('from-', '').replace('to-', ', ')}) 1` }">
    </div>
    
    <!-- 点击提示 -->
    <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
      <div class="p-3 rounded-full bg-black/50 backdrop-blur-sm">
        <i class="fa fa-search-plus text-white"></i>
      </div>
    </div>
  </div>
</template>