<!-- src/views/NewsView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import NewsSection from '@/components/NewsSection.vue'
</script>

<template>
  <div class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-blue-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent">
            游戏资讯
          </span>
        </h1>
        <p class="text-gray-400">获取最新的游戏更新与公告</p>
      </div>

      <!-- 资讯内容 -->
      <NewsSection :fullView="true" />
    </div>
  </div>
</template>