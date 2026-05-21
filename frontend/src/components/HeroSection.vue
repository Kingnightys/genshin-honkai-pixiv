<script setup lang="ts">
const scrollToSection = (sectionId: string) => {
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>

<template>
  <section id="home" class="min-h-screen flex items-center justify-center pt-20 px-4">
    <div class="text-center">
      <h1 class="text-5xl md:text-7xl font-bold mb-6">
        <span class="bg-gradient-to-r from-purple-400 via-pink-400 to-blue-400 bg-clip-text text-transparent">
          原神 / 星穹铁道
        </span>
      </h1>
      <p class="text-xl text-gray-300 mb-8">探索提瓦特与星际的无限可能</p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <button 
          class="px-8 py-4 bg-gradient-to-r from-purple-500 to-blue-500 rounded-xl font-bold hover:opacity-90 transition-all"
          @click="scrollToSection('characters')"
        >
          探索角色
        </button>
        <button 
          class="px-8 py-4 border-2 border-white/30 rounded-xl font-bold hover:bg-white/10 transition-all"
          @click="scrollToSection('banner')"
        >
          查看卡池
        </button>
      </div>
    </div>
  </section>
</template>
