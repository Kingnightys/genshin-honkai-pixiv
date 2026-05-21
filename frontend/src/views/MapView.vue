<!-- src/views/MapView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import MapSection from '@/components/MapSection.vue'
</script>

<template>
  <div class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">
          <span class="bg-gradient-to-r from-cyan-400 via-blue-400 to-purple-400 bg-clip-text text-transparent">
            地图探索
          </span>
        </h1>
        <p class="text-gray-400">探索提瓦特与星际的各个角落</p>
      </div>

      <!-- 地图内容 -->
      <MapSection :fullView="true" />
    </div>
  </div>
</template>