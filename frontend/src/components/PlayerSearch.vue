<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

interface PlayerData {
  uid: string
  nickname: string
  level: number
  worldLevel: number
  characters: string[]
}

const uid = ref('')
const playerData = ref<PlayerData | null>(null)
const isLoading = ref(false)

// Mock数据
const mockPlayer: PlayerData = {
  uid: '100000001',
  nickname: '旅行者',
  level: 60,
  worldLevel: 8,
  characters: ['钟离', '雷电将军', '神里绫华']
}

const searchPlayer = async () => {
  if (!uid.value || uid.value.length !== 9) {
    alert('请输入9位UID')
    return
  }

  isLoading.value = true
  try {
    const response = await axios.get(`http://192.168.8.49:8000/api/player/${uid.value}`)
    playerData.value = response.data.data || mockPlayer
  } catch {
    playerData.value = { ...mockPlayer, uid: uid.value }
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <section id="search" class="py-20 px-4">
    <div class="max-w-3xl mx-auto">
      <h2 class="text-4xl font-bold text-center mb-12">UID查询</h2>
      <div class="bg-slate-800/50 rounded-xl p-8 border border-slate-700">
        <div class="flex gap-4 mb-6">
          <input 
            v-model="uid" 
            type="text" 
            placeholder="输入9位UID"
            maxlength="9"
            class="flex-1 bg-slate-700 border border-slate-600 rounded-xl px-4 py-3 focus:border-purple-500 outline-none"
            @keyup.enter="searchPlayer"
          />
          <button 
            class="px-8 py-3 bg-gradient-to-r from-purple-500 to-blue-500 rounded-xl font-bold hover:opacity-90 transition-all"
            :disabled="isLoading"
            @click="searchPlayer"
          >
            <span v-if="isLoading" class="flex items-center gap-2">
              <i class="fa fa-spinner fa-spin"></i> 查询中
            </span>
            <span v-else>查询</span>
          </button>
        </div>
        
        <div v-if="playerData" class="bg-slate-700/50 rounded-xl p-6">
          <h3 class="font-bold text-xl mb-4">{{ playerData.nickname }}</h3>
          <p class="text-gray-400 mb-2">UID: {{ playerData.uid }}</p>
          <p class="text-gray-400 mb-4">冒险等级: {{ playerData.level }}</p>
          <h4 class="font-bold mb-2">角色:</h4>
          <div class="flex flex-wrap gap-2">
            <span 
              v-for="char in playerData.characters" 
              :key="char"
              class="px-3 py-1 bg-purple-500/20 text-purple-400 rounded-full text-sm"
            >
              {{ char }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
