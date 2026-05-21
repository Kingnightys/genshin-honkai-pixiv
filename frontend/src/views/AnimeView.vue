<!-- src/views/AnimeView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AnimeSection from '@/components/AnimeSection.vue'
</script>

<template>
  <div class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-yellow-400 via-orange-400 to-red-400 bg-clip-text text-transparent">
            官方番剧
          </span>
        </h1>
        <p class="text-gray-400">观看原神与星穹铁道的官方动画</p>
      </div>

      <!-- 番剧内容 -->
      <AnimeSection :fullView="true" />
    </div>
  </div>
</template>