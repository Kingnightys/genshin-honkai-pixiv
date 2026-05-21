<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Message {
  id: number
  nickname: string
  content: string
  created_at: number
}

const messages = ref<Message[]>([])
const newNickname = ref('')
const newContent = ref('')
const isLoading = ref(true)

// Mock数据
const mockMessages: Message[] = [
  { id: 1, nickname: '旅行者', content: '这个网站太棒了！', created_at: Date.now() / 1000 - 3600 },
  { id: 2, nickname: '星穹骑士', content: '期待更多精彩内容！', created_at: Date.now() / 1000 - 7200 },
]

const formatTime = (timestamp: number) => {
  const diff = Date.now() / 1000 - timestamp
  const hours = Math.floor(diff / 3600)
  const days = Math.floor(hours / 24)
  
  if (hours < 1) return '刚刚'
  if (hours < 24) return `${hours}小时前`
  if (days < 7) return `${days}天前`
  return new Date(timestamp * 1000).toLocaleDateString('zh-CN')
}

const fetchMessages = async () => {
  try {
    const response = await axios.get('http://192.168.8.49:8000/api/messages')
    messages.value = response.data.data || mockMessages
  } catch {
    messages.value = mockMessages
  } finally {
    isLoading.value = false
  }
}

const addMessage = async () => {
  if (!newNickname.value.trim() || !newContent.value.trim()) {
    alert('请填写昵称和留言内容')
    return
  }

  try {
    const response = await axios.post('http://192.168.8.49:8000/api/messages', {
      nickname: newNickname.value,
      content: newContent.value
    })
    
    if (response.data.data) {
      messages.value.unshift(response.data.data)
    } else {
      messages.value.unshift({
        id: Date.now(),
        nickname: newNickname.value,
        content: newContent.value,
        created_at: Date.now() / 1000
      })
    }
    
    newNickname.value = ''
    newContent.value = ''
  } catch {
    messages.value.unshift({
      id: Date.now(),
      nickname: newNickname.value,
      content: newContent.value,
      created_at: Date.now() / 1000
    })
    newNickname.value = ''
    newContent.value = ''
  }
}

onMounted(() => {
  fetchMessages()
})
</script>

<template>
  <section id="message" class="py-20 px-4">
    <div class="max-w-3xl mx-auto">
      <h2 class="text-4xl font-bold text-center mb-12">留言板</h2>
      
      <div class="bg-slate-800/50 rounded-xl p-6 border border-slate-700 mb-6">
        <input 
          v-model="newNickname" 
          type="text" 
          placeholder="你的昵称"
          class="w-full bg-slate-700 border border-slate-600 rounded-xl px-4 py-3 mb-3 focus:border-purple-500 outline-none"
        />
        <textarea 
          v-model="newContent" 
          placeholder="留下你的留言..."
          rows="3"
          class="w-full bg-slate-700 border border-slate-600 rounded-xl px-4 py-3 mb-3 focus:border-purple-500 outline-none resize-none"
        ></textarea>
        <button 
          class="w-full py-3 bg-gradient-to-r from-purple-500 to-blue-500 rounded-xl font-bold hover:opacity-90 transition-all"
          @click="addMessage"
        >
          发表留言
        </button>
      </div>

      <div v-if="isLoading" class="flex justify-center">
        <div class="w-10 h-10 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="space-y-4">
        <div 
          v-for="msg in messages" 
          :key="msg.id"
          class="bg-slate-800/50 rounded-xl p-4 border border-slate-700"
        >
          <div class="flex items-center justify-between mb-2">
            <span class="font-bold text-purple-400">{{ msg.nickname }}</span>
            <span class="text-xs text-gray-500">{{ formatTime(msg.created_at) }}</span>
          </div>
          <p>{{ msg.content }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
