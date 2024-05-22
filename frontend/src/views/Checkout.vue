<script lang="ts" setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { useCartStore } from "@/store/cart";

const router = useRouter();
const cartStore = useCartStore();

const tableHeaders = [
  { title: "Title", key: "title" },
  { title: "Author", key: "author" },
];

const loading = ref(false);

const reserve = () => {
  loading.value = true;

  const data: any = {
    items: [],
  };

  cartStore.items.forEach((item: any) => {
    data.items.push({ item: item.id });
  });

  axios
    .post("/api/v1/checkout/", data)
    .then(() => {
      cartStore.items = [];
      localStorage.setItem("cart", JSON.stringify(cartStore.items));
      router.push("/success");
    })
    .catch((error) => {
      console.log(error);
    })
    .finally(() => (loading.value = false));
};
</script>

<template>
  <v-container>
    <v-data-table :headers="tableHeaders" :items="cartStore.items">
      <template #top>
        <v-toolbar title="Cart" density="compact" color="primary" />
      </template>
      <template #bottom></template>
    </v-data-table>
    <v-btn variation="text" @click="reserve"> Reserve the items </v-btn>
  </v-container>
</template>
