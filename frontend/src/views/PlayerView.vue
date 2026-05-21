<!-- src/views/PlayerView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import PlayerSearch from '@/components/PlayerSearch.vue'
</script>

<template>
  <div class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-green-400 via-blue-400 to-purple-400 bg-clip-text text-transparent">
            玩家查询
          </span>
        </h1>
        <p class="text-gray-400">输入UID查询玩家信息</p>
      </div>

      <!-- 玩家查询内容 -->
      <PlayerSearch :fullView="true" />
    </div>
  </div>
</template>