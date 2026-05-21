<!-- src/views/MusicView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import MusicSection from '@/components/MusicSection.vue'
</script>

<template>
  <div class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-purple-400 via-pink-400 to-red-400 bg-clip-text text-transparent">
            音乐专辑
          </span>
        </h1>
        <p class="text-gray-400">聆听游戏中的优美旋律</p>
      </div>

      <!-- 音乐内容 -->
      <MusicSection :fullView="true" />
    </div>
  </div>
</template>