<template>
  <div>
    <form @submit.prevent="submitForm">
      <label for="username">Nazwa użytkownika:</label>
      <input type="text" id="username" v-model="username" required>

      <label for="password">Hasło:</label>
      <input type="password" id="password" v-model="password" required>

      <button type="submit">Zaloguj się</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import CryptoJS from 'crypto-js';

export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async submitForm() {
      const oneTimeKey = CryptoJS.lib.WordArray.random(128/8).toString(CryptoJS.enc.Hex);
      const hashedPassword = CryptoJS.SHA256(this.password + oneTimeKey).toString(CryptoJS.enc.Hex);

      try {
        const response = await axios.post('http://localhost:5000/api/login', {
          username: this.username,
          password: hashedPassword,
          oneTimeKey: oneTimeKey
        });

        if (response.data.success) {
          console.log('Zalogowano');
        } else {
          console.log('Niepoprawne dane logowania');
        }
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>
