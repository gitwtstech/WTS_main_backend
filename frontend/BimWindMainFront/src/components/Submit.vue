<script setup lang="ts">
    import { ref } from 'vue';
    import axios from 'axios';

    const email = ref('');
    const password = ref('');
    const id = ref('');

    type user = {
      id: number;
      username: string;
    }

    type GetUsersResponse = {
      data: user[];
    }
    
    async function submit(email: string, password: string) {
      const {data, status} = await axios.post<user>(`http://127.0.0.1:8000/api/v1/users/`, 
      {
        username: email,
      },
      {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      })
      printResult(data, status)
      return status;
    }

    async function getUsers(){
      const {data, status} = await axios.get<GetUsersResponse>("http://127.0.0.1:8000/api/v1/users/", 
      {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      });
      printResult(data, status)
      return data;
    }

    async function getUserById(id: number){
      console.log("http://127.0.0.1:8000/api/v1/users/"+id);
      const {data, status} = await axios.get<user>("http://127.0.0.1:8000/api/v1/users/"+id, 
      {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      });
      printResult(data, status)
      return data;
    }

    async function delUserById(id: number){
      console.log("http://127.0.0.1:8000/api/v1/users/"+id);
      const {data, status} = await axios.delete<user>("http://127.0.0.1:8000/api/v1/users/"+id, 
      {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      });
      printResult(data, status)
      return data;
    }

    function printResult(data: any, status: number) {
      console.log(status)
      console.log(JSON.stringify(data, null, 4));
    }

</script>
<template>
    <div class="submit">
      <form action="" aria-orientation="vertical">
        <input v-model="email" name="email" type="email" placeholder="email...">
        <input v-model="password" name="password" type="password" placeholder="*********">
        <button name="Submit" type="submit" @click="submit(email, password)">Submit</button>
        <button name="GetUsers" type="button" @click="getUsers()">Получить пользователей</button>
        <input v-model="id" name="id" placeholder="ID">
        <button name="GetUserById" type="button" @click="getUserById(id)">Получить пользователя по ID</button>
        <button name="DeleteUserById" type="button" @click="delUserById(id)">Удалить пользователя по ID</button>
      </form>
    </div>
</template>

<style>
input {
    display: block;
    align-content: center;
    margin: 10px;
    padding: 5px;
  }

.submit {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}
</style>