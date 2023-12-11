<template>
  <UserLogin msg="Welcome to Your Vue.js App"/>
  <br>
  <br>
  <br>
  <GreetingsAjax />
</template>

<script>
import UserLogin from './components/user-login.vue'
import GreetingsAjax from './components/greetings-ajax.vue';

export default {
  name: 'App',
  components: {
    UserLogin,
    GreetingsAjax
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
