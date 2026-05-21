<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Activity {
  id: number
  title: string
  description: string
  image: string
  endTime: string
}

const activities = ref<Activity[]>([])
const isLoading = ref(true)

// Mock数据
const mockActivities: Activity[] = [
  { id: 1, title: '风花节', description: '蒙德的春日庆典', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=windblume%20festival%20genshin&width=400&height=200', endTime: '2024-03-15' },
  { id: 2, title: '深渊螺旋', description: '挑战极限，获取丰厚奖励', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=spiral%20abyss%20genshin&width=400&height=200', endTime: '永久' },
  { id: 3, title: '星穹铁道活动', description: '探索新的星球', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=honkai%20star%20rail%20event&width=400&height=200', endTime: '2024-03-20' },
]

const fetchActivities = async () => {
  try {
    const response = await axios.get('http://192.168.8.49:8000/api/activities/genshin')
    activities.value = response.data.data || mockActivities
  } catch {
    activities.value = mockActivities
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchActivities()
})
</script>

<template>
  <section id="activities" class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-4xl font-bold text-center mb-12">活动中心</h2>

      <div v-if="isLoading" class="flex justify-center">
        <div class="w-10 h-10 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div 
          v-for="activity in activities" 
          :key="activity.id"
          class="bg-slate-800/50 rounded-xl overflow-hidden border border-slate-700 hover:border-purple-500/50 transition-all cursor-pointer"
        >
          <img :src="activity.image" :alt="activity.title" class="w-full h-32 object-cover" />
          <div class="p-4">
            <h3 class="font-bold text-lg mb-2">{{ activity.title }}</h3>
            <p class="text-gray-400 text-sm mb-3">{{ activity.description }}</p>
            <span class="text-xs text-purple-400">截止: {{ activity.endTime }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
