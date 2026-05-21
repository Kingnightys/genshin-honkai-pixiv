<template>
  <div 
    class="character-card group relative bg-slate-800/40 backdrop-blur-sm rounded-2xl p-5 border border-slate-700/50 cursor-pointer transform transition-all duration-500 hover:-translate-y-2 hover:shadow-2xl hover:border-purple-500/50"
    @click="$emit('select', character)"
  >
    <!-- 背景渐变 -->
    <div class="absolute inset-0 rounded-2xl bg-gradient-to-br opacity-0 group-hover:opacity-100 transition-opacity duration-500"
         :style="{ background: `linear-gradient(to bottom right, ${elementColor}20, ${elementColor}40)` }">
    </div>
    
    <!-- 内容 -->
    <div class="relative z-10 flex flex-col items-center">
      <!-- 头像 -->
      <div class="relative mb-3">
        <img 
          :src="character.local_path" 
          :alt="character.name"
          class="w-16 h-16 sm:w-20 sm:h-20 rounded-full object-cover border-3 border-slate-600 group-hover:border-purple-400 transition-colors duration-300"
          @error="handleImageError"
        />
        <!-- 稀有度 -->
        <div class="absolute -bottom-1 left-1/2 transform -translate-x-1/2 flex gap-0.5">
          <span 
            v-for="i in character.rarity" 
            :key="i"
            class="text-yellow-400 text-sm sm:text-base drop-shadow-md"
          >★</span>
        </div>
      </div>
      
      <!-- 名称 -->
      <h3 class="text-white font-semibold text-sm sm:text-base mb-2 text-center truncate w-full">
        {{ character.name }}
      </h3>
      
      <!-- 标签 -->
      <div class="flex flex-wrap justify-center gap-1.5">
        <span 
          class="px-2 py-0.5 rounded-full text-xs font-medium"
          :style="{ backgroundColor: elementColor + '30', color: elementColor }"
        >
          {{ character.element }}
        </span>
        <span 
          v-if="character.path"
          class="px-2 py-0.5 rounded-full text-xs font-medium bg-slate-700/50 text-slate-300"
        >
          {{ character.path }}
        </span>
      </div>
      
      <!-- 版本 -->
      <span class="text-slate-500 text-xs mt-2">v{{ character.version }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Character {
  name: string
  element: string
  path?: string
  rarity: number
  version: string
  local_path: string
  description?: string
}

const props = defineProps<{
  character: Character
}>()

defineEmits<{
  select: [character: Character]
}>()

const ELEMENT_COLORS: Record<string, string> = {
  '风': '#87CEEB', '火': '#FF6B6B', '水': '#4ECDC4', '冰': '#A8D8EA', '雷': '#DDA0DD', '岩': '#CD853F', '草': '#90EE90',
  '物理': '#C0C0C0', '虚数': '#9370DB', '量子': '#FFD700', '存护': '#FFA500', '巡猎': '#FF4500', '智识': '#1E90FF',
  '虚无': '#9400D3', '丰饶': '#32CD32', '同谐': '#FF69B4'
}

const elementColor = computed(() => ELEMENT_COLORS[props.character.element] || '#9370DB')

const handleImageError = (e: Event) => {
  const target = e.target as HTMLImageElement
  target.style.display = 'none'
}
</script>

<style scoped>
.character-card {
  min-height: 140px;
}
</style>