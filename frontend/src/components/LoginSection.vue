<template>
  <section class="login-section min-h-screen flex items-center justify-center py-8">
    <div class="container mx-auto px-4">
      <div class="max-w-md w-full">
        <!-- Logo -->
        <div class="text-center mb-8">
          <div class="w-20 h-20 mx-auto rounded-xl bg-gradient-to-br from-purple-500 via-pink-500 to-orange-500 flex items-center justify-center text-3xl shadow-lg">
            🎮
          </div>
          <h1 class="text-2xl font-bold text-white mt-4">欢迎回来</h1>
          <p class="text-slate-400 mt-2">登录你的账号</p>
        </div>
        
        <!-- 登录表单 -->
        <div class="bg-slate-800/50 rounded-2xl p-6 border border-slate-700/50">
          <form @submit.prevent="handleLogin">
            <div class="mb-4">
              <label class="block text-slate-400 text-sm mb-2">邮箱</label>
              <input 
                v-model="email"
                type="email"
                placeholder="请输入邮箱"
                class="w-full px-4 py-3 bg-slate-700/50 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:border-purple-500 transition-colors"
              />
            </div>
            <div class="mb-6">
              <label class="block text-slate-400 text-sm mb-2">密码</label>
              <input 
                v-model="password"
                type="password"
                placeholder="请输入密码"
                class="w-full px-4 py-3 bg-slate-700/50 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:border-purple-500 transition-colors"
              />
            </div>
            <button 
              type="submit"
              :disabled="isLoading"
              class="w-full px-6 py-3 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 disabled:bg-slate-600 disabled:cursor-not-allowed text-white rounded-lg font-medium transition-all duration-300 flex items-center justify-center gap-2"
            >
              <span v-if="isLoading" class="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></span>
              <span v-else>登录</span>
            </button>
          </form>
          
          <!-- 分割线 -->
          <div class="flex items-center gap-4 my-6">
            <div class="flex-1 h-px bg-slate-700"></div>
            <span class="text-slate-500 text-sm">或</span>
            <div class="flex-1 h-px bg-slate-700"></div>
          </div>
          
          <!-- 社交登录 -->
          <div class="grid grid-cols-2 gap-4">
            <button class="px-4 py-3 bg-blue-600/20 hover:bg-blue-600/30 border border-blue-600/30 rounded-lg text-blue-400 font-medium transition-all duration-300 flex items-center justify-center gap-2">
              <svg class="w-5 h-5" viewBox="0 0 24 24">
                <path fill="currentColor" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                <path fill="currentColor" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                <path fill="currentColor" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                <path fill="currentColor" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
              </svg>
              Google
            </button>
            <button class="px-4 py-3 bg-green-600/20 hover:bg-green-600/30 border border-green-600/30 rounded-lg text-green-400 font-medium transition-all duration-300 flex items-center justify-center gap-2">
              <svg class="w-5 h-5" viewBox="0 0 24 24">
                <path fill="currentColor" d="M20.283 10.356h-8.327v3.451h4.792c-.446 2.193-2.313 3.453-4.792 3.453a5.27 5.27 0 0 1-5.279-5.28 5.27 5.27 0 0 1 5.279-5.279c1.259 0 2.397.447 3.29 1.178l2.6-2.599c-1.584-1.381-3.615-2.233-5.89-2.233a8.908 8.908 0 0 0-8.934 8.934 8.907 8.907 0 0 0 8.934 8.934c4.467 0 8.529-3.249 8.529-8.934 0-.528-.081-1.097-.202-1.625z"/>
              </svg>
              GitHub
            </button>
          </div>
          
          <!-- 注册链接 -->
          <p class="text-center text-slate-400 text-sm mt-6">
            还没有账号？
            <button class="text-purple-400 hover:text-purple-300 transition-colors">注册</button>
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const email = ref('')
const password = ref('')
const isLoading = ref(false)

const emit = defineEmits(['login'])

const handleLogin = async () => {
  if (!email.value || !password.value) {
    alert('请输入邮箱和密码')
    return
  }
  
  isLoading.value = true
  
  try {
    const response = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: email.value, password: password.value })
    })
    
    if (response.ok) {
      const data = await response.json()
      localStorage.setItem('token', data.token)
      emit('login')
    } else {
      alert('登录失败，请检查邮箱和密码')
    }
  } catch (error) {
    console.error('登录失败:', error)
    // 模拟登录成功
    localStorage.setItem('token', 'mock-token')
    emit('login')
  } finally {
    isLoading.value = false
  }
}
</script>