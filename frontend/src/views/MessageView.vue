<!-- src/views/MessageView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import MessageSection from '@/components/MessageSection.vue'
</script>

<template>
  <div class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-purple-400 via-pink-400 to-red-400 bg-clip-text text-transparent">
            留言板
          </span>
        </h1>
        <p class="text-gray-400">留下您的宝贵意见和建议</p>
      </div>

      <!-- 留言内容 -->
      <MessageSection :fullView="true" />
    </div>
  </div>
</template>