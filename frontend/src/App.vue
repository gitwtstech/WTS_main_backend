<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './/components/NavBar.vue'
</script>

<template>
  <NavBar />
  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

</style>
