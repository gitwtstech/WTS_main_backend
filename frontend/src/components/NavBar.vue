<script setup lang="ts">
import {RouterLink } from "vue-router"

</script>
<template>
    <header>
    <div class="container-fluid">
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid justify-content-start">
          <RouterLink to="/" class="navbar-brand">
            <img src="../assets/logo.svg" class="float-start" alt="BIMWIND" style="height: 2rem;">
          </RouterLink>
          
        </div>
        <div class="nav nav-underline container-fluid justify-content-end">
          <RouterLink to="/about" class="nav-link">О нас</RouterLink>
          <RouterLink to="/courses" class="nav-link">Курсы</RouterLink>
          <RouterLink to="/plugins" class="nav-link">Плагины</RouterLink>
          <RouterLink to="/components" class="nav-link">Библиотека компонентов</RouterLink>
          <RouterLink to="/auth/login" class="nav-link">Логин</RouterLink>
        </div>
      </nav>
    </div>
      
  
  </header>
</template>