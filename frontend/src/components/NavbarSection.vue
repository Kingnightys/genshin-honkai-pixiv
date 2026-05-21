<!-- d:\AiCodeProject\genshin-honkai-pixiv\frontend\src\components\NavbarSection.vue -->
<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const isMobileMenuOpen = ref(false)

const navItems = [
  { path: '/', label: '首页', icon: 'fa-home', badge: null },
  { path: '/characters', label: '角色图鉴', icon: 'fa-users', badge: '新' },
  { path: '/banner', label: '祈愿卡池', icon: 'fa-gem', badge: 'UP' },
  { path: '/activities', label: '限时活动', icon: 'fa-calendar', badge: null },
  { path: '/news', label: '游戏资讯', icon: 'fa-newspaper', badge: 'Hot' },
  { path: '/music', label: '原声音乐', icon: 'fa-music', badge: null },
  { path: '/pv', label: '宣传PV', icon: 'fa-video', badge: null },
  { path: '/fanart', label: '同人创作', icon: 'fa-palette', badge: null },
  { path: '/map', label: '地图打卡', icon: 'fa-map', badge: null },
  { path: '/anime', label: '番剧馆', icon: 'fa-play-circle', badge: null },
  { path: '/player', label: 'UID查询', icon: 'fa-search', badge: null },
  { path: '/message', label: '留言板', icon: 'fa-comments', badge: null },
]

const currentPath = computed(() => route.path)

const navigateTo = (path: string) => {
  isMobileMenuOpen.value = false
  router.push(path)
}

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}
</script>

<template>
  <nav class="fixed w-full top-0 left-0 right-0 z-50 bg-gradient-to-r from-slate-900/95 via-slate-900/95 to-slate-900/95 border-b border-purple-500/15">
    <!-- 内容层 -->
    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
      <!-- Logo + 用户操作区域 -->
      <div class="flex items-center justify-between mb-3">
        <!-- Logo区域 -->
        <div class="flex items-center gap-3 cursor-pointer group" @click="navigateTo('/')">
          <div class="relative">
            <div class="absolute inset-[-4px] bg-gradient-to-br from-purple-500 via-pink-500 to-cyan-500 rounded-full blur-md opacity-40 group-hover:opacity-60 transition-opacity"></div>
            <div class="relative w-10 h-10 bg-gradient-to-br from-purple-600 via-pink-500 to-cyan-500 rounded-full flex items-center justify-center shadow-lg shadow-purple-500/30 group-hover:scale-105 transition-transform">
              <div class="flex items-center gap-0.5">
                <i class="fa fa-sun text-yellow-200 text-xs"></i>
                <i class="fa fa-star text-cyan-200 text-xs"></i>
              </div>
            </div>
          </div>
          <div>
            <span class="text-lg font-bold bg-gradient-to-r from-purple-400 via-pink-400 to-cyan-400 bg-clip-text text-transparent">
              提瓦特·星际
            </span>
            <span class="hidden sm:block text-xs text-gray-500 ml-1">Genshin × Star Rail</span>
          </div>
        </div>

        <!-- 用户操作区域 -->
        <div class="flex items-center gap-2">
          <button class="p-2 rounded-lg hover:bg-white/10 transition-all group">
            <i class="fa fa-search text-gray-400 group-hover:text-white"></i>
          </button>
          <button class="relative p-2 rounded-lg hover:bg-white/10 transition-all group">
            <i class="fa fa-bell text-gray-400 group-hover:text-white"></i>
            <span class="absolute top-0.5 right-0.5 w-1.5 h-1.5 bg-red-500 rounded-full"></span>
          </button>
          <button v-if="authStore.isLoggedIn"
            class="px-4 py-2 rounded-lg bg-white/8 hover:bg-white/15 transition-all flex items-center gap-2 border border-white/10"
            @click="handleLogout">
            <i class="fa fa-user-circle text-gray-400 text-sm"></i>
            <span class="text-sm font-medium text-gray-300">退出</span>
          </button>
          <button v-else
            class="px-4 py-2 rounded-lg bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500 hover:opacity-90 transition-all flex items-center gap-2 shadow-lg shadow-purple-500/30"
            @click="navigateTo('/login')">
            <i class="fa fa-sign-in text-white text-sm"></i>
            <span class="text-sm font-medium text-white">登录</span>
          </button>
        </div>

        <!-- 移动端菜单按钮 -->
        <button class="lg:hidden p-2.5 rounded-lg hover:bg-white/10 transition-all" @click="isMobileMenuOpen = !isMobileMenuOpen">
          <i :class="`fa ${isMobileMenuOpen ? 'fa-times text-lg' : 'fa-bars text-lg'} text-gray-300`"></i>
        </button>
      </div>

      <!-- 导航菜单 -->
      <div class="hidden lg:flex items-center justify-center gap-2">
        <button 
          v-for="item in navItems" 
          :key="item.path"
          class="relative px-4 py-2 rounded-lg font-medium transition-all duration-300 flex items-center gap-2"
          :class="currentPath === item.path 
            ? 'text-white bg-gradient-to-r from-purple-500/20 to-blue-500/20 shadow-md shadow-purple-500/15' 
            : 'text-gray-300 hover:text-white hover:bg-white/8'"
          @click="navigateTo(item.path)"
        >
          <i :class="[`fa ${item.icon} text-sm`,currentPath === item.path ? 'text-purple-300' : '']"></i>
          <span class="whitespace-nowrap">{{ item.label }}</span>
          <span v-if="item.badge" class="px-1.5 py-0.25 text-xs font-bold rounded-full"
            :class="item.badge === 'Hot' ? 'bg-gradient-to-r from-red-500 to-orange-500 text-white' :
              item.badge === 'UP' ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white' :
                'bg-gradient-to-r from-cyan-500 to-blue-500 text-white'">
            {{ item.badge }}
          </span>
          <div v-if="currentPath === item.path"
            class="absolute bottom-0 left-1/2 -translate-x-1/2 w-5 h-0.5 rounded-full bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500"
          ></div>
        </button>
      </div>

      <!-- 移动端菜单 -->
      <div v-if="isMobileMenuOpen" class="lg:hidden mt-4 pb-4 border-t border-slate-700/50 pt-4">
        <div class="grid grid-cols-4 gap-2 mb-4">
          <button v-for="item in navItems" :key="item.path"
            class="flex flex-col items-center gap-1 p-3 rounded-xl transition-all"
            :class="currentPath === item.path 
              ? 'bg-gradient-to-br from-purple-500/30 to-blue-500/30 text-white' 
              : 'text-gray-400 hover:bg-white/10 hover:text-white'"
            @click="navigateTo(item.path)">
            <div class="w-9 h-9 rounded-lg flex items-center justify-center" :class="currentPath === item.path ? 'bg-white/20' : 'bg-white/5'">
              <i :class="`fa ${item.icon} text-base`"></i>
            </div>
            <span class="text-xs font-medium">{{ item.label }}</span>
            <span v-if="item.badge" class="px-1.5 py-0.25 text-xs font-bold rounded-full"
              :class="item.badge === 'Hot' ? 'bg-red-500 text-white' :
                item.badge === 'UP' ? 'bg-purple-500 text-white' :
                  'bg-cyan-500 text-white'">
              {{ item.badge }}
            </span>
          </button>
        </div>

        <div class="flex gap-3">
          <button v-if="authStore.isLoggedIn"
            class="flex-1 px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/15 transition-all flex items-center justify-center gap-2"
            @click="handleLogout">
            <i class="fa fa-sign-out"></i>
            <span>退出登录</span>
          </button>
          <button v-else
            class="flex-1 px-4 py-2.5 rounded-xl bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500 hover:opacity-90 transition-all flex items-center justify-center gap-2"
            @click="navigateTo('/login')">
            <i class="fa fa-sign-in"></i>
            <span>登录</span>
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>