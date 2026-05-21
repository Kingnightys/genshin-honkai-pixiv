<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Banner {
  id: number
  name: string
  type: string
  version: string
  image: string
}

const banners = ref<Banner[]>([])
const isLoading = ref(true)

// Mock数据
const mockBanners: Banner[] = [
  { id: 1, name: '钟离', type: '角色', version: '4.0', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=zhongli%20genshin%20banner%20art&width=300&height=400' },
  { id: 2, name: '雷电将军', type: '角色', version: '4.0', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=raiden%20shogun%20genshin%20banner%20art&width=300&height=400' },
  { id: 3, name: '武器祈愿', type: '武器', version: '4.0', image: 'https://neeko-copilot.bytedance.net/api/text2image?prompt=genshin%20weapon%20banner%20art&width=300&height=400' },
]

const fetchBanners = async () => {
  try {
    const response = await axios.get('http://192.168.8.49:8000/api/banner/genshin')
    banners.value = response.data.data || mockBanners
  } catch {
    banners.value = mockBanners
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchBanners()
})
</script>

<template>
  <section id="banner" class="py-20 px-4">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-4xl font-bold text-center mb-12">卡池祈愿</h2>
      
      <div v-if="isLoading" class="flex justify-center">
        <div class="w-10 h-10 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div 
          v-for="banner in banners" 
          :key="banner.id"
          class="bg-slate-800/50 rounded-2xl overflow-hidden border border-slate-700 hover:border-purple-500/50 transition-all hover:scale-105"
        >
          <img :src="banner.image" :alt="banner.name" class="w-full h-64 object-cover" />
          <div class="p-4">
            <div class="flex items-center gap-2 mb-2">
              <span class="px-2 py-1 bg-purple-500/20 text-purple-400 rounded text-sm">{{ banner.type }}</span>
              <span class="text-gray-400 text-sm">版本 {{ banner.version }}</span>
            </div>
            <h3 class="text-xl font-bold">{{ banner.name }}</h3>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
