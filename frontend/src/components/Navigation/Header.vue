<script setup lang="ts">
import { ref } from "vue";
import { useDisplay } from "vuetify";
import Login from "@/components/Navigation/Login.vue";
import Cart from "@/components/Navigation/Cart.vue";

const { mobile } = useDisplay({ mobileBreakpoint: 768 });

const menuItems = [
  {
    title: "Category",
    slug: "/items",
  },
  {
    title: "All Items",
    slug: "/items",
  },
];

const drawerOpen = ref(false);
</script>

<template>
  <v-container class="w-100 h-48 pa-0 elevation-10">
    <v-app-bar
      dark
      color="primary"
      density="compact"
      class="px-2 d-flex justify-space-between"
    >
      <template v-if="mobile" v-slot:prepend>
        <v-app-bar-nav-icon @click.stop="drawerOpen = !drawerOpen" />
      </template>

      <v-row v-if="!mobile" align="center" no-gutters>
        <v-col cols="auto">
          <v-btn variant="plain" to="/">LIBRARY SYSTEM</v-btn>
        </v-col>
        <v-spacer />
        <v-col v-for="(item, i) in menuItems" :key="i" cols="auto">
          <v-btn variant="plain" :to="item.slug">
            {{ item.title }}
          </v-btn>
        </v-col>
        <v-spacer />
        <v-col cols="auto">
          <v-row no-gutters>
            <v-col cols="auto">
              <Login />
            </v-col>
            <v-col cols="auto">
              <Cart />
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-app-bar>

    <v-overlay
      v-model="drawerOpen"
      :close-on-content-click="true"
      location-strategy="connected"
      scroll-strategy="block"
    >
      <v-row
        location="top start"
        class="pa-4 h-screen bg-primary d-flex flex-column flex-grow-1"
      >
        <v-list class="pa-2 bg-primary">
          <v-list-item
            v-for="item in menuItems"
            :title="item.title"
            link
            :to="item.slug"
            class="pa-2 bg-primary"
          />
        </v-list>
        <Login class="mb-6" />
        <Cart />
      </v-row>
    </v-overlay>
  </v-container>
</template>
