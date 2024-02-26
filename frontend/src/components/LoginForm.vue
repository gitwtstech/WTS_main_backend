<template>
    <div class="container-sm mb-3 text-center card">
      <div class="row g-3 ">
        <input type="email" class="form-control" name="" aria-describedby="emailHelpId" placeholder="email" id="inputGroup1">
        <input type="password" class="form-control" name="" aria-describedby="emailHelpId" placeholder="Пароль" id="inputGroup2">
        <div class="col-sm">
            <button type="submit" class="btn btn-primary">Войти</button>
        </div>
        <div class="row">
            <div class="col-sm">
                <label>У вас еще нет аккаунта? <RouterLink to="/auth/register">Создать аккаунт</RouterLink></label>
            </div>
        </div>
      </div>
    </div>
</template>

