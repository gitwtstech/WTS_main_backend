<script setup lang="ts">
import { userAPI, type User } from '../scripts/APIDataService';

const user: User = {
  username: '',
  password: '',
  email: ''
}

</script>

<template>
    <div class="container-sm mb-3 text-center card">
      <div class="row g-3 ">
        <input itemid="0" v-model="user.username" type="email" class="form-control" placeholder="email" id="inputGroup1">
        <input v-model="user.email" type="text" class="form-control" placeholder="Имя пользователя" id="inputGroup2">
        <input v-model="user.password" type="password" class="form-control" placeholder="Пароль" id="inputGroup3">
        <div class="col-sm">
            <button type="submit" class="btn btn-primary" @click="userAPI.post(user)">Зарегистрироваться</button>
        </div>
        <div class="row g-2 text-center">
            <RouterLink to="/auth/login">У меня уже есть аккаунт</RouterLink>
        </div>
      </div>
      <button type="button" class="btn btn-secondary" @click="userAPI.get()">Получить пользвателей</button>
    </div>
</template>../scripts/APIDataService