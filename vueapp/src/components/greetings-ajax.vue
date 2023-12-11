<template>
  <div>
    <input v-model="name" placeholder="Enter your name">
    <button @click="getGreeting">Get Greeting</button>
    <p v-if="greeting">{{ greeting }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      greeting: ''
    }
  },
  methods: {
    async getGreeting() {
      try {
        const response = await axios.post('http://localhost:5000/api/greeting', { name: this.name });
        this.greeting = response.data.greeting;
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>
