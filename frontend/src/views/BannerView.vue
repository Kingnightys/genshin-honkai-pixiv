<!-- src/views/BannerView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import BannerSection from '@/components/BannerSection.vue'
</script>

<template>
  <div class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-pink-400 via-purple-400 to-blue-400 bg-clip-text text-transparent">
            祈愿卡池
          </span>
        </h1>
        <p class="text-gray-400">查看最新的祈愿活动与限定角色</p>
      </div>

      <!-- 卡池内容 -->
      <BannerSection :fullView="true" />
    </div>
  </div>
</template>