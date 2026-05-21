<!-- src/views/ActivitiesView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import ActivitiesSection from '@/components/ActivitiesSection.vue'
</script>

<template>
  <div class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-green-400 via-cyan-400 to-blue-400 bg-clip-text text-transparent">
            游戏活动
          </span>
        </h1>
        <p class="text-gray-400">参与限时活动，获取丰厚奖励</p>
      </div>

      <!-- 活动内容 -->
      <ActivitiesSection :fullView="true" />
    </div>
  </div>
</template>