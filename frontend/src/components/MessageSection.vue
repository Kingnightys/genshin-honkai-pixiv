<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getMessages, createMessage } from '@/api'
import type { Message } from '@/types'

defineProps<{
  fullView?: boolean
}>()

const messages = ref<Message[]>([])
const nickname = ref('')
const email = ref('')
const content = ref('')
const isSubmitting = ref(false)
const isLoading = ref(false)

const fetchMessages = async () => {
  isLoading.value = true
  try {
    messages.value = await getMessages()
  } catch (error) {
    console.error('获取留言失败:', error)
    // 使用Mock数据
    messages.value = [
      {
        id: 1,
        user_id: 1,
        nickname: '旅行者',
        email: 'traveler@example.com',
        content: '原神真的很好玩！期待枫丹的更新！',
        created_at: Date.now() / 1000 - 3600
      },
      {
        id: 2,
        user_id: 2,
        nickname: '开拓者',
        email: 'trailblazer@example.com',
        content: '星穹铁道的剧情太棒了，景元大人无敌！',
        created_at: Date.now() / 1000 - 7200
      }
    ]
  } finally {
    isLoading.value = false
  }
}

const handleSubmit = async () => {
  if (!nickname.value || !content.value) {
    alert('请填写昵称和留言内容')
    return
  }
  
  isSubmitting.value = true
  try {
    const newMessage = await createMessage({
      nickname: nickname.value,
      email: email.value,
      content: content.value
    })
    messages.value.unshift(newMessage)
    nickname.value = ''
    email.value = ''
    content.value = ''
    alert('留言成功')
  } catch (error) {
    console.error('创建留言失败:', error)
    alert('留言失败，请重试')
  } finally {
    isSubmitting.value = false
  }
}

const formatTime = (timestamp: number): string => {
  const date = new Date(timestamp * 1000)
  const now = new Date()
  const diff = now.getTime() - date.getTime()
  
  if (diff < 60000) return '刚刚'
  if (diff < 3600000) return `${Math.floor(diff / 60000)}分钟前`
  if (diff < 86400000) return `${Math.floor(diff / 3600000)}小时前`
  if (diff < 604800000) return `${Math.floor(diff / 86400000)}天前`
  
  return date.toLocaleDateString('zh-CN')
}

onMounted(() => {
  fetchMessages()
})
</script>

<template>
  <section id="message" class="py-12 px-4">
    <div class="max-w-3xl mx-auto">
      <!-- 标题 -->
      <div class="text-center mb-8">
        <h2 class="text-2xl lg:text-3xl font-bold mb-2">
          <span class="bg-gradient-to-r from-purple-400 via-pink-400 to-red-400 bg-clip-text text-transparent">
            留言板
          </span>
        </h2>
        <p class="text-gray-400">留下您的宝贵意见</p>
      </div>

      <!-- 留言表单 -->
      <div class="bg-white/5 backdrop-blur-md rounded-2xl p-6 mb-8 border border-white/10">
        <h3 class="text-lg font-medium mb-4">发表留言</h3>
        <form @submit.prevent="handleSubmit" class="space-y-4">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-300 text-sm mb-2">昵称 *</label>
              <input
                v-model="nickname"
                type="text"
                placeholder="请输入昵称"
                class="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-purple-500 transition-colors"
              />
            </div>
            <div>
              <label class="block text-gray-300 text-sm mb-2">邮箱（选填）</label>
              <input
                v-model="email"
                type="email"
                placeholder="请输入邮箱"
                class="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-purple-500 transition-colors"
              />
            </div>
          </div>
          <div>
            <label class="block text-gray-300 text-sm mb-2">留言内容 *</label>
            <textarea
              v-model="content"
              rows="4"
              placeholder="请输入留言内容..."
              class="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-purple-500 transition-colors resize-none"
            ></textarea>
          </div>
          <button
            type="submit"
            :disabled="isSubmitting"
            class="w-full py-3 bg-gradient-to-r from-purple-500 via-pink-500 to-red-500 rounded-xl font-medium text-white hover:opacity-90 transition-all disabled:opacity-50 flex items-center justify-center gap-2"
          >
            <i v-if="isSubmitting" class="fa fa-spinner animate-spin"></i>
            {{ isSubmitting ? '提交中...' : '发表留言' }}
          </button>
        </form>
      </div>

      <!-- 留言列表 -->
      <div v-if="isLoading" class="flex justify-center py-8">
        <div class="w-8 h-8 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="space-y-4">
        <div
          v-for="message in messages"
          :key="message.id"
          class="group bg-slate-800/50 backdrop-blur-sm rounded-2xl p-5 border border-slate-700/50 hover:border-purple-500/30 transition-all duration-300"
        >
          <div class="flex items-start gap-4">
            <!-- 用户头像 -->
            <div class="relative">
              <div class="w-12 h-12 rounded-full bg-gradient-to-br from-purple-500 via-pink-500 to-blue-500 flex items-center justify-center flex-shrink-0 shadow-lg shadow-purple-500/30">
                <i class="fa fa-user text-white text-lg"></i>
              </div>
              <div class="absolute -bottom-1 -right-1 w-4 h-4 bg-green-500 rounded-full border-2 border-slate-800"></div>
            </div>
            <!-- 留言内容 -->
            <div class="flex-1">
              <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-white group-hover:text-purple-300 transition-colors">
                  {{ message.nickname }}
                </span>
                <span class="text-xs text-gray-500 flex items-center gap-1">
                  <i class="fa fa-clock"></i>
                  {{ formatTime(message.created_at) }}
                </span>
              </div>
              <p class="text-gray-300 leading-relaxed">{{ message.content }}</p>
            </div>
          </div>
        </div>

        <!-- 空状态 -->
        <div v-if="messages.length === 0" class="text-center py-12">
          <div class="w-20 h-20 mx-auto mb-4 rounded-full bg-gradient-to-br from-purple-500/20 to-blue-500/20 flex items-center justify-center">
            <i class="fa fa-comments text-4xl text-gray-500"></i>
          </div>
          <p class="text-gray-400">暂无留言，快来发表第一条留言吧！</p>
        </div>
      </div>
    </div>
  </section>
</template>