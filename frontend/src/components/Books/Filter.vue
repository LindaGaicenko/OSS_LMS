<script setup lang="ts">
  import { ref } from 'vue'

  const filterOpen = ref(false)
</script>

<template>
  <v-card>
    <v-card-title @click.stop="filterOpen = !filterOpen"> Filter & Sort </v-card-title>
    <v-menu
      v-model="filterOpen"
      transition="slide-y-transition"
      :close-on-content-click="false"
      location="end"
    >
      <v-container class="bg-primary h-screen">
        <v-icon
          icon="mdi-close"
          @click.stop="filterOpen = !filterOpen"
        />
        <v-row
          location="top start"
          class="w-100"
        >
          <v-col>
            <v-select label="Sort By" />
          </v-col>
        </v-row>
      </v-container>
    </v-menu>
  </v-card>
</template>
