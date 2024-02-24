<script setup lang="ts">
import { ref } from 'vue';
import { userAPI } from '../scripts/getDataAPI';

const user = new userAPI();
const username = ref('');
const password = ref('');
const email = ref('');


</script>

<template>
    <div class="container-sm mb-3 text-center card">
      <div class="row g-3 ">
        <input itemid="0" v-model="username" type="email" class="form-control" placeholder="email">
        <input v-model="email" type="text" class="form-control" placeholder="Имя пользователя">
        <input v-model="password" type="password" class="form-control" placeholder="Пароль">
        <div class="col-sm">
            <button type="submit" class="btn btn-primary" @click="user.post(email, username, password)">Зарегистрироваться</button>
        </div>
        <div class="row g-2 text-center">
            <a href="/auth/login">У меня уже есть аккаунт</a>
        </div>
      </div>
      <button type="button" class="btn btn-secondary" @click="user.get()">Получить пользвателей</button>
    </div>
</template>