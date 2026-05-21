<template>
  <section class="home-section">
    <!-- Hero区域 -->
    <div class="relative h-[70vh] bg-gradient-to-br from-slate-900 via-purple-900/20 to-slate-900 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <div class="absolute top-1/4 left-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl animate-pulse"></div>
        <div class="absolute bottom-1/4 right-1/4 w-80 h-80 bg-pink-500/10 rounded-full blur-3xl animate-pulse" style="animation-delay: 1s"></div>
      </div>
      
      <div class="relative z-10 text-center px-4">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-white/10 backdrop-blur-sm rounded-full mb-6">
          <span class="w-2 h-2 bg-green-400 rounded-full animate-pulse"></span>
          <span class="text-sm text-white/80">原神 · 星穹铁道 数据平台</span>
        </div>
        <h1 class="text-4xl md:text-6xl font-bold mb-6">
          <span class="bg-gradient-to-r from-purple-400 via-pink-400 to-orange-400 bg-clip-text text-transparent">
            探索提瓦特与星际
          </span>
        </h1>
        <p class="text-slate-400 text-lg mb-8">一站式获取原神和星穹铁道的角色信息、卡池动态、活动资讯</p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <button 
            @click="$emit('navigate', 'characters')"
            class="px-8 py-4 bg-gradient-to-r from-purple-600 via-pink-600 to-orange-600 text-white rounded-xl font-medium transition-all duration-300 shadow-lg"
          >
            🎭 浏览角色图鉴
          </button>
          <button 
            @click="$emit('navigate', 'banner')"
            class="px-8 py-4 bg-slate-800/80 text-white rounded-xl font-medium transition-all duration-300 border border-slate-600/50"
          >
            🎁 查看最新卡池
          </button>
        </div>
      </div>
    </div>
    
    <!-- 快捷入口 -->
    <div class="container mx-auto px-4 py-12">
      <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-4">
        <div 
          v-for="entry in quickEntries" 
          :key="entry.id"
          @click="$emit('navigate', entry.id)"
          class="bg-slate-800/50 rounded-2xl p-5 border border-slate-700/50 hover:border-purple-500/50 transition-all duration-300 cursor-pointer hover:-translate-y-2"
        >
          <div 
            class="w-14 h-14 rounded-xl flex items-center justify-center text-3xl mb-4"
            :style="{ background: entry.gradient + '30' }"
          >
            {{ entry.icon }}
          </div>
          <h3 class="text-white font-medium text-center text-sm">{{ entry.name }}</h3>
          <p class="text-slate-400 text-xs text-center mt-1">{{ entry.desc }}</p>
        </div>
      </div>
    </div>
    
    <!-- 统计数据 -->
    <div class="bg-gradient-to-r from-purple-600/10 via-pink-600/10 to-orange-600/10 py-12">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
          <div v-for="stat in stats" :key="stat.label" class="text-center">
            <div class="text-3xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent mb-2">
              {{ stat.value }}
            </div>
            <div class="text-slate-400 text-sm">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 最新资讯 -->
    <div class="container mx-auto px-4 py-12">
      <div class="flex items-center justify-between mb-8">
        <h2 class="text-2xl font-bold text-white">
          <span class="bg-gradient-to-r from-red-400 to-orange-400 bg-clip-text text-transparent">
            最新资讯
          </span>
        </h2>
        <button @click="$emit('navigate', 'news')" class="text-purple-400 hover:text-purple-300 text-sm flex items-center gap-1">
          查看全部
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </div>
      
      <div class="grid md:grid-cols-3 gap-6">
        <div 
          v-for="news in latestNews" 
          :key="news.id"
          @click="$emit('navigate', 'news')"
          class="bg-slate-800/50 rounded-xl p-5 border border-slate-700/50 cursor-pointer hover:border-red-500/30 transition-all duration-300"
        >
          <span 
            class="inline-block px-2 py-1 text-xs rounded-full mb-3"
            :class="news.type === 'update' ? 'bg-blue-500/20 text-blue-400' : 'bg-green-500/20 text-green-400'"
          >
            {{ news.type === 'update' ? '版本更新' : '活动公告' }}
          </span>
          <h3 class="text-white font-medium mb-2">{{ news.title }}</h3>
          <p class="text-slate-400 text-sm">{{ news.desc }}</p>
          <div class="text-slate-500 text-xs mt-3">{{ news.date }}</div>
        </div>
      </div>
    </div>
    
    <!-- 当前卡池 -->
    <div class="container mx-auto px-4 py-12">
      <div class="flex items-center justify-between mb-8">
        <h2 class="text-2xl font-bold text-white">
          <span class="bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
            当前卡池
          </span>
        </h2>
        <button @click="$emit('navigate', 'banner')" class="text-purple-400 hover:text-purple-300 text-sm flex items-center gap-1">
          查看详情
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </div>
      
      <div class="grid md:grid-cols-2 gap-6">
        <div class="bg-gradient-to-br from-orange-600/20 to-red-600/10 rounded-xl p-6 border border-orange-500/20">
          <div class="flex items-center gap-2 mb-4">
            <span class="text-xl">🌄</span>
            <span class="text-white font-medium">原神</span>
          </div>
          <div class="flex items-center gap-4">
            <div class="w-16 h-16 rounded-xl bg-gradient-to-br from-orange-500/30 to-red-500/30 flex items-center justify-center text-2xl font-bold text-white">
              芙
            </div>
            <div>
              <p class="text-white font-medium">当前UP: <span class="text-orange-400">芙宁娜</span></p>
              <p class="text-slate-400 text-sm">陪跑: 夏洛蒂</p>
            </div>
          </div>
        </div>
        
        <div class="bg-gradient-to-br from-purple-600/20 to-blue-600/10 rounded-xl p-6 border border-purple-500/20">
          <div class="flex items-center gap-2 mb-4">
            <span class="text-xl">🚀</span>
            <span class="text-white font-medium">星穹铁道</span>
          </div>
          <div class="flex items-center gap-4">
            <div class="w-16 h-16 rounded-xl bg-gradient-to-br from-purple-500/30 to-blue-500/30 flex items-center justify-center text-2xl font-bold text-white">
              黄
            </div>
            <div>
              <p class="text-white font-medium">当前UP: <span class="text-purple-400">黄泉</span></p>
              <p class="text-slate-400 text-sm">陪跑: 缇宝</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
defineEmits(['navigate'])

const quickEntries = [
  { id: 'characters', name: '角色图鉴', icon: '🎭', desc: '浏览所有角色', gradient: 'linear-gradient(to right, #f093fb, #f5576c)' },
  { id: 'banner', name: '卡池查询', icon: '🎁', desc: '查看卡池信息', gradient: 'linear-gradient(to right, #4facfe, #00f2fe)' },
  { id: 'player', name: '玩家查询', icon: '👤', desc: '查询玩家数据', gradient: 'linear-gradient(to right, #43e97b, #38f9d7)' },
  { id: 'activities', name: '活动日历', icon: '🎯', desc: '最新活动', gradient: 'linear-gradient(to right, #fa709a, #fee140)' },
  { id: 'news', name: '游戏资讯', icon: '📰', desc: '官方公告', gradient: 'linear-gradient(to right, #ff9a9e, #fecfef)' },
  { id: 'pv', name: 'PV视频', icon: '🎬', desc: '精彩PV', gradient: 'linear-gradient(to right, #a18cd1, #fbc2eb)' },
  { id: 'music', name: '游戏音乐', icon: '🎵', desc: '原声音乐', gradient: 'linear-gradient(to right, #ffecd2, #fcb69f)' },
  { id: 'fanart', name: '同人作品', icon: '🎨', desc: '社区创作', gradient: 'linear-gradient(to right, #667eea, #764ba2)' }
]

const stats = [
  { label: '原神角色', value: '72+' },
  { label: '星铁角色', value: '45+' },
  { label: '活动资讯', value: '100+' },
  { label: 'PV视频', value: '50+' }
]

const latestNews = [
  { id: 1, title: '4.4版本「彩鹞栉春风」更新公告', desc: '全新角色闲云、嘉明登场', type: 'update', date: '2024-01-24' },
  { id: 2, title: '海灯节活动「磬弦奏华夜」即将开启', desc: '参与活动获取丰厚奖励', type: 'event', date: '2024-01-25' },
  { id: 3, title: '星穹铁道2.3版本「寰宇蝗灾」更新', desc: '全新角色缇宝登场', type: 'update', date: '2024-01-23' }
]
</script>