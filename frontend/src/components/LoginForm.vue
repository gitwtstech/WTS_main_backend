<template>
    <div class="container-sm mb-3 text-center card">
      <div class="row g-3 ">
        <input type="email" class="form-control" name="" id="" aria-describedby="emailHelpId" placeholder="email">
        <input type="password" class="form-control" name="" id="" aria-describedby="emailHelpId" placeholder="Пароль">
        <div class="col-sm">
            <button type="submit" class="btn btn-primary">Войти</button>
        </div>
        <div class="row">
            <div class="col-sm g-2">
                <label>У вас еще нет аккаунта?</label>
                <RouterLink to="/auth/register">Создать аккаунт</RouterLink>
            </div>
        </div>
      </div>
    </div>
</template>

