<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const footerLinks = [
  { label: '角色图鉴', path: '/characters' },
  { label: '祈愿卡池', path: '/banner' },
  { label: '游戏资讯', path: '/news' },
  { label: '音乐专辑', path: '/music' },
  { label: '同人作品', path: '/fanart' },
  { label: '留言反馈', path: '/message' },
]

const socialLinks = [
  { icon: 'fa-github', label: 'GitHub', url: '#' },
  { icon: 'fa-twitter', label: 'Twitter', url: '#' },
  { icon: 'fa-discord', label: 'Discord', url: '#' },
  { icon: 'fa-youtube', label: 'YouTube', url: '#' },
]

const navigateTo = (path: string) => {
  router.push(path)
}
</script>

<template>
  <footer class="relative bg-gradient-to-b from-slate-900/95 via-slate-900 to-slate-950 border-t border-white/5">
    <!-- 装饰背景 -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-0 left-1/4 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl"></div>
      <div class="absolute bottom-0 right-1/4 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl"></div>
    </div>
    
    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <!-- 主内容区域 -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <!-- Logo和简介 -->
        <div class="lg:col-span-1">
          <div class="flex items-center gap-3 mb-4">
            <div class="w-10 h-10 bg-gradient-to-br from-purple-500 via-pink-500 to-blue-500 rounded-xl flex items-center justify-center shadow-lg shadow-purple-500/30">
              <i class="fa fa-gamepad text-white"></i>
            </div>
            <span class="text-xl font-bold bg-gradient-to-r from-purple-400 via-pink-400 to-blue-400 bg-clip-text text-transparent">
              原神/星穹铁道
            </span>
          </div>
          <p class="text-gray-400 text-sm leading-relaxed">
            探索提瓦特大陆与星际世界的无限可能，这里是原神与星穹铁道爱好者的聚集地。
          </p>
          <!-- 社交媒体 -->
          <div class="flex items-center gap-3 mt-6">
            <a 
              v-for="social in socialLinks"
              :key="social.label"
              :href="social.url"
              :aria-label="social.label"
              class="w-10 h-10 rounded-xl bg-white/5 hover:bg-gradient-to-r hover:from-purple-500/20 hover:to-blue-500/20 flex items-center justify-center transition-all duration-300 group"
            >
              <i :class="`fa ${social.icon} text-gray-400 group-hover:text-white transition-colors`"></i>
            </a>
          </div>
        </div>

        <!-- 快速链接 -->
        <div>
          <h4 class="text-white font-semibold mb-4 flex items-center gap-2">
            <i class="fa fa-link text-purple-400"></i>
            快速导航
          </h4>
          <ul class="space-y-2">
            <li v-for="link in footerLinks" :key="link.label">
              <button 
                class="text-gray-400 hover:text-white hover:pl-2 transition-all duration-300 flex items-center gap-2 group"
                @click="navigateTo(link.path)"
              >
                <i class="fa fa-chevron-right text-xs opacity-0 group-hover:opacity-100 transition-opacity"></i>
                {{ link.label }}
              </button>
            </li>
          </ul>
        </div>

        <!-- 游戏信息 -->
        <div>
          <h4 class="text-white font-semibold mb-4 flex items-center gap-2">
            <i class="fa fa-gamepad text-pink-400"></i>
            游戏信息
          </h4>
          <ul class="space-y-2">
            <li class="text-gray-400 text-sm flex items-center gap-2">
              <i class="fa fa-sun text-yellow-400"></i>
              <span>原神 v4.2</span>
            </li>
            <li class="text-gray-400 text-sm flex items-center gap-2">
              <i class="fa fa-star text-cyan-400"></i>
              <span>星穹铁道 v1.6</span>
            </li>
            <li class="text-gray-400 text-sm flex items-center gap-2">
              <i class="fa fa-users text-purple-400"></i>
              <span>活跃玩家 10万+</span>
            </li>
          </ul>
        </div>

        <!-- 联系我们 -->
        <div>
          <h4 class="text-white font-semibold mb-4 flex items-center gap-2">
            <i class="fa fa-envelope text-blue-400"></i>
            联系我们
          </h4>
          <ul class="space-y-3">
            <li class="text-gray-400 text-sm flex items-center gap-2">
              <i class="fa fa-envelope"></i>
              <span>contact@genshin-honkai.com</span>
            </li>
            <li class="text-gray-400 text-sm flex items-center gap-2">
              <i class="fa fa-clock"></i>
              <span>周一至周日 9:00-22:00</span>
            </li>
          </ul>
          <!-- 订阅 -->
          <div class="mt-4">
            <p class="text-gray-400 text-sm mb-2">订阅最新资讯</p>
            <div class="flex gap-2">
              <input 
                type="email" 
                placeholder="输入邮箱"
                class="flex-1 px-4 py-2 bg-white/5 border border-white/10 rounded-lg text-white placeholder-gray-500 text-sm focus:outline-none focus:border-purple-500"
              />
              <button class="px-4 py-2 bg-gradient-to-r from-purple-500 to-blue-500 rounded-lg text-white text-sm hover:opacity-90 transition-opacity">
                订阅
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- 分隔线 -->
      <div class="mt-10 pt-8 border-t border-white/5">
        <div class="flex flex-col md:flex-row items-center justify-between gap-4">
          <div class="flex flex-wrap items-center justify-center gap-4 text-sm text-gray-500">
            <span>© 2026 原神/星穹铁道爱好者社区</span>
            <span>|</span>
            <button class="hover:text-white transition-colors">隐私政策</button>
            <span>|</span>
            <button class="hover:text-white transition-colors">用户协议</button>
            <span>|</span>
            <button class="hover:text-white transition-colors">联系我们</button>
          </div>
          <div class="flex items-center gap-2 text-sm text-gray-500">
            <span>Made with</span>
            <i class="fa fa-heart text-red-500 animate-pulse"></i>
            <span>by Genshin/Honkai Fans</span>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>