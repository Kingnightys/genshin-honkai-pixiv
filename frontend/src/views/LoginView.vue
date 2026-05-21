<!-- d:\AiCodeProject\genshin-honkai-pixiv\frontend\src\views\LoginView.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import LoginSection from '@/components/LoginSection.vue'

const router = useRouter()
const authStore = useAuthStore()

const isLoginMode = ref(true)

const handleLogin = async (username: string, password: string) => {
  try {
    await authStore.login(username, password)
    router.push('/')
  } catch (err) {
    console.error('登录失败:', err)
  }
}

const handleRegister = async (username: string, email: string, password: string) => {
  try {
    await authStore.register(username, email, password)
    router.push('/')
  } catch (err) {
    console.error('注册失败:', err)
  }
}

const handleGuestLogin = () => {
  // 游客登录，设置默认用户
  authStore.user = { username: '游客', email: '' }
  authStore.isLoggedIn = true
  localStorage.setItem('user', JSON.stringify({ username: '游客', email: '' }))
  router.push('/')
}

const handleModeChange = (mode: boolean) => {
  isLoginMode.value = mode
}

onMounted(() => {
  // 如果已登录，跳转到首页
  if (authStore.isLoggedIn) {
    router.push('/')
  }
})
</script>

<template>
  <div class="min-h-screen flex items-center justify-center px-4 py-12 relative overflow-hidden">
    <!-- 背景装饰 -->
    <div class="absolute inset-0">
      <!-- 渐变背景 -->
      <div class="absolute inset-0 bg-gradient-to-br from-slate-900 via-purple-900/40 to-slate-900"></div>
      <!-- 动态粒子 -->
      <div class="absolute inset-0 overflow-hidden">
        <div v-for="i in 30" :key="i" 
          class="absolute rounded-full animate-float"
          :style="{
            width: Math.random() * 15 + 5 + 'px',
            height: Math.random() * 15 + 5 + 'px',
            background: `rgba(${Math.random() > 0.5 ? '168, 85, 247' : '236, 72, 153'}, ${Math.random() * 0.5 + 0.2})`,
            left: Math.random() * 100 + '%',
            top: Math.random() * 100 + '%',
            animationDelay: Math.random() * 5 + 's',
            animationDuration: Math.random() * 15 + 10 + 's'
          }"
        ></div>
      </div>
      <!-- 光晕效果 -->
      <div class="absolute top-1/3 left-1/4 w-80 h-80 bg-purple-500/15 rounded-full blur-3xl"></div>
      <div class="absolute bottom-1/3 right-1/4 w-80 h-80 bg-pink-500/15 rounded-full blur-3xl"></div>
    </div>

    <!-- 登录卡片 -->
    <div class="relative z-10 w-full max-w-md">
      <!-- 顶部装饰 -->
      <div class="text-center mb-8">
        <div class="inline-flex items-center gap-3 mb-4">
          <div class="relative">
            <div class="w-14 h-14 bg-gradient-to-br from-purple-500 via-pink-500 to-cyan-500 rounded-xl flex items-center justify-center shadow-xl shadow-purple-500/40">
              <i class="fa fa-gamepad text-white text-2xl"></i>
            </div>
            <div class="absolute inset-0 bg-gradient-to-br from-purple-500 via-pink-500 to-cyan-500 rounded-xl blur-lg opacity-50"></div>
          </div>
        </div>
        <h1 class="text-3xl font-bold bg-gradient-to-r from-purple-400 via-pink-400 to-cyan-400 bg-clip-text text-transparent">
          {{ isLoginMode ? '欢迎回来' : '创建账号' }}
        </h1>
        <p class="text-gray-400 mt-2">
          {{ isLoginMode ? '登录您的账户，开启冒险之旅' : '注册新账户，探索奇幻世界' }}
        </p>
      </div>

      <!-- 引入登录组件 -->
      <LoginSection 
        @login="handleLogin"
        @register="handleRegister"
        @guest-login="handleGuestLogin"
        @mode-change="handleModeChange"
      />

      <!-- 底部提示 -->
      <p class="text-center text-gray-500 text-sm mt-6">
        登录即表示同意我们的
        <button class="text-purple-400 hover:text-purple-300">服务条款</button>
        和
        <button class="text-purple-400 hover:text-purple-300">隐私政策</button>
      </p>
    </div>
  </div>
</template>

<style scoped>
@keyframes float {
  0%, 100% {
    transform: translateY(0) translateX(0);
    opacity: 0.3;
  }
  25% {
    transform: translateY(-30px) translateX(10px);
    opacity: 0.8;
  }
  50% {
    transform: translateY(-20px) translateX(-10px);
    opacity: 0.5;
  }
  75% {
    transform: translateY(-40px) translateX(5px);
    opacity: 0.7;
  }
}

.animate-float {
  animation: float 15s ease-in-out infinite;
}
</style>