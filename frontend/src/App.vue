<script setup lang="ts">
  import { onBeforeMount } from 'vue'
  import Header from '@/components/Navigation/Header.vue'
  import { useAppStore } from './store/app'
  import axios from 'axios'

  const appStore = useAppStore()

  onBeforeMount(() => {
    const token = appStore.user.token

    if (token) {
      axios.defaults.headers.Authorization = `Token ${token}`
    } else {
      axios.defaults.headers.Authorization = ''
    }
  })
</script>

<template>
  <v-app>
    <v-main>
      <Header />
      <router-view />
    </v-main>
  </v-app>
</template>
