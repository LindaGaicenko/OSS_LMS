<script setup lang="ts">
  import { useAppStore } from '@/store/app'

  const appStore = useAppStore()
</script>

<template>
  <div>
    <v-btn
      v-if="appStore.isLoggedIn"
      append-icon="mdi-menu-down"
      color="white"
      variant="text"
      to="/account"
    >
      My Account
    </v-btn>
    <v-btn
      v-else
      variant="text"
      color="white"
      to="/login"
    >
      Login / Register
    </v-btn>
  </div>
</template>
