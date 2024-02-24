<script setup lang="ts">
    import { ref } from 'vue';
    import axios from 'axios';
    const username = ref('');
    const password = ref('');
    const email = ref('');
    type User = {
        username: string,
        password: string,
        email: string
    }

    type GetUsers = {
        users: User[]
    }
    async function register(email:string, username: string, password: string){
        const {data, status} = await axios.post<User>("http://127.0.0.1:8000/api/v1/users/", 
        {username: username},  
        {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });

        console.log(JSON.stringify(data, null, 4));

        console.log(status);
    };
    async function getUsers(){
        const {data, status} = await axios.get<GetUsers>("http://127.0.0.1:8000/api/v1/users/",{
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        })
        console.log(JSON.stringify(data, null, 4));

        console.log(status);
    };
</script>

<template>
    <div class="container-sm mb-3 text-center card">
      <div class="row g-3 ">
        <input itemid="0" v-model="username" type="email" class="form-control" placeholder="email">
        <input v-model="email" type="text" class="form-control" placeholder="Имя пользователя">
        <input v-model="password" type="password" class="form-control" placeholder="Пароль">
        <div class="col-sm">
            <button type="submit" class="btn btn-primary" @click="register(email, username, password)">Зарегистрироваться</button>
        </div>
        <div class="row g-2 text-center">
            <a href="/auth/login">У меня уже есть аккаунт</a>
        </div>
      </div>
      <button type="button" class="btn btn-secondary" @click="getUsers">Получить пользвателей</button>
    </div>
</template>