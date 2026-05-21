<!-- src/views/PvView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import PvSection from '@/components/PvSection.vue'
</script>

<template>
  <div class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-orange-400 via-red-400 to-purple-400 bg-clip-text text-transparent">
            宣传PV
          </span>
        </h1>
        <p class="text-gray-400">观看精彩的游戏宣传视频</p>
      </div>

      <!-- PV内容 -->
      <PvSection :fullView="true" />
    </div>
  </div>
</template>