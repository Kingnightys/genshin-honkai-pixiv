<!-- src/components/LoginSection.vue -->
<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits<{
  login: [username: string, password: string]
  register: [username: string, email: string, password: string]
  guestLogin: []
  'mode-change': [isLoginMode: boolean]
}>()

const isLoginMode = ref(true)
const username = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const isLoading = ref(false)
const errorMessage = ref('')
const showPassword = ref(false)

const handleSubmit = async () => {
  errorMessage.value = ''
  
  if (isLoginMode.value) {
    if (!username.value || !password.value) {
      errorMessage.value = '请填写用户名和密码'
      return
    }
    isLoading.value = true
    try {
      emit('login', username.value, password.value)
    } finally {
      isLoading.value = false
    }
  } else {
    if (!username.value || !email.value || !password.value) {
      errorMessage.value = '请填写所有必填字段'
      return
    }
    if (password.value.length < 6) {
      errorMessage.value = '密码长度至少6位'
      return
    }
    if (password.value !== confirmPassword.value) {
      errorMessage.value = '两次输入的密码不一致'
      return
    }
    isLoading.value = true
    try {
      emit('register', username.value, email.value, password.value)
    } finally {
      isLoading.value = false
    }
  }
}

const toggleMode = () => {
  isLoginMode.value = !isLoginMode.value
  username.value = ''
  email.value = ''
  password.value = ''
  confirmPassword.value = ''
  errorMessage.value = ''
  emit('mode-change', isLoginMode.value)
}

const handleGuestLogin = () => {
  emit('guestLogin')
}
</script>

<template>
  <div class="bg-white/5 backdrop-blur-xl rounded-2xl p-8 border border-white/10 shadow-2xl shadow-purple-500/10 w-full max-w-md">
    <!-- 错误提示 -->
    <div v-if="errorMessage" class="mb-6 p-4 bg-red-500/10 border border-red-500/30 rounded-xl flex items-center gap-2 text-red-400">
      <i class="fa fa-exclamation-circle"></i>
      <span>{{ errorMessage }}</span>
    </div>

    <!-- 切换标签 -->
    <div class="flex mb-8 bg-white/10 rounded-xl p-1">
      <button
        class="flex-1 py-3 px-4 rounded-lg font-medium transition-all duration-300"
        :class="isLoginMode ? 'bg-gradient-to-r from-purple-500 to-cyan-500 text-white shadow-lg shadow-purple-500/30' : 'text-gray-400 hover:text-white hover:bg-white/5'"
        @click="toggleMode"
      >
        <span class="flex items-center justify-center gap-2">
          <i class="fa fa-sign-in"></i>
          登录
        </span>
      </button>
      <button
        class="flex-1 py-3 px-4 rounded-lg font-medium transition-all duration-300"
        :class="!isLoginMode ? 'bg-gradient-to-r from-purple-500 to-cyan-500 text-white shadow-lg shadow-purple-500/30' : 'text-gray-400 hover:text-white hover:bg-white/5'"
        @click="toggleMode"
      >
        <span class="flex items-center justify-center gap-2">
          <i class="fa fa-user-plus"></i>
          注册
        </span>
      </button>
    </div>

    <!-- 表单 -->
    <form @submit.prevent="handleSubmit" class="space-y-5">
      <!-- 用户名 -->
      <div>
        <label class="block text-gray-300 mb-2 text-sm font-medium">用户名</label>
        <div class="relative">
          <i class="absolute left-4 top-1/2 -translate-y-1/2 fa fa-user text-gray-400"></i>
          <input
            v-model="username"
            type="text"
            placeholder="请输入用户名"
            class="w-full pl-12 pr-4 py-3.5 bg-white/10 border border-white/20 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-purple-500 focus:ring-1 focus:ring-purple-500/50 transition-all"
          />
        </div>
      </div>

      <!-- 邮箱（注册模式） -->
      <div v-if="!isLoginMode">
        <label class="block text-gray-300 mb-2 text-sm font-medium">邮箱</label>
        <div class="relative">
          <i class="absolute left-4 top-1/2 -translate-y-1/2 fa fa-envelope text-gray-400"></i>
          <input
            v-model="email"
            type="email"
            placeholder="请输入邮箱"
            class="w-full pl-12 pr-4 py-3.5 bg-white/10 border border-white/20 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-purple-500 focus:ring-1 focus:ring-purple-500/50 transition-all"
          />
        </div>
      </div>

      <!-- 密码 -->
      <div>
        <label class="block text-gray-300 mb-2 text-sm font-medium">密码</label>
        <div class="relative">
          <i class="absolute left-4 top-1/2 -translate-y-1/2 fa fa-lock text-gray-400"></i>
          <input
            v-model="password"
            :type="showPassword ? 'text' : 'password'"
            placeholder="请输入密码"
            class="w-full pl-12 pr-12 py-3.5 bg-white/10 border border-white/20 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-purple-500 focus:ring-1 focus:ring-purple-500/50 transition-all"
          />
          <button
            type="button"
            class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white transition-colors"
            @click="showPassword = !showPassword"
          >
            <i :class="`fa ${showPassword ? 'fa-eye-slash' : 'fa-eye'}`"></i>
          </button>
        </div>
      </div>

      <!-- 确认密码（注册模式） -->
      <div v-if="!isLoginMode">
        <label class="block text-gray-300 mb-2 text-sm font-medium">确认密码</label>
        <div class="relative">
          <i class="absolute left-4 top-1/2 -translate-y-1/2 fa fa-lock text-gray-400"></i>
          <input
            v-model="confirmPassword"
            :type="showPassword ? 'text' : 'password'"
            placeholder="请再次输入密码"
            class="w-full pl-12 pr-4 py-3.5 bg-white/10 border border-white/20 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-purple-500 focus:ring-1 focus:ring-purple-500/50 transition-all"
          />
        </div>
      </div>

      <!-- 记住我（登录模式） -->
      <div v-if="isLoginMode" class="flex items-center justify-between">
        <label class="flex items-center gap-2 cursor-pointer">
          <input type="checkbox" class="w-4 h-4 rounded border-gray-600 bg-white/10 text-purple-500 focus:ring-purple-500/50" />
          <span class="text-gray-400 text-sm">记住我</span>
        </label>
        <button class="text-purple-400 hover:text-purple-300 text-sm transition-colors">
          忘记密码？
        </button>
      </div>

      <!-- 提交按钮 -->
      <button
        type="submit"
        :disabled="isLoading"
        class="w-full py-4 bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500 rounded-xl font-bold text-lg text-white hover:opacity-90 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 shadow-lg shadow-purple-500/30 hover:shadow-purple-500/50"
      >
        <i v-if="isLoading" class="fa fa-spinner animate-spin"></i>
        {{ isLoading ? (isLoginMode ? '登录中...' : '注册中...') : (isLoginMode ? '登录' : '注册') }}
      </button>
    </form>

    <!-- 切换链接 -->
    <p class="text-center text-gray-400 mt-6">
      {{ isLoginMode ? '还没有账号？' : '已有账号？' }}
      <button @click="toggleMode" class="text-purple-400 hover:text-purple-300 ml-1 font-medium transition-colors">
        {{ isLoginMode ? '立即注册' : '立即登录' }}
      </button>
    </p>

    <!-- 分隔线 -->
    <div class="flex items-center gap-4 my-6">
      <div class="flex-1 h-px bg-gradient-to-r from-transparent via-white/20 to-transparent"></div>
      <span class="text-gray-400 text-sm">或</span>
      <div class="flex-1 h-px bg-gradient-to-r from-transparent via-white/20 to-transparent"></div>
    </div>

    <!-- 游客登录 -->
    <button 
      class="w-full py-3.5 bg-white/10 border border-white/20 rounded-xl hover:bg-white/15 transition-all flex items-center justify-center gap-2 group"
      @click="handleGuestLogin"
    >
      <i class="fa fa-user-circle text-xl text-gray-400 group-hover:text-white transition-colors"></i>
      <span class="text-gray-300 group-hover:text-white transition-colors">游客登录</span>
    </button>
  </div>
</template>