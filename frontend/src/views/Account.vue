<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import { useAppStore } from "@/store/app";
import axios from "axios";
import moment from "moment";

const appStore = useAppStore();
const router = useRouter();

const reservationHeaders = [
  { title: "ID", key: "id" },
  {
    title: "Date & Time",
    key: "created_at",
    value: ({ created_at }: { created_at: string }) =>
      moment(created_at).format("YYYY-MM-DD hh:mm"),
  },
  {
    title: "Status",
    key: "status",
    value: ({ status }: { status: string }) => {
      switch (status) {
        case "new":
          return "New";
        case "active":
          return "Active";
        case "done":
          return "Done";
        case "cancelled":
          return "Cancelled";
        default:
          return "";
      }
    },
  },
];

const loading = ref(false);
const reservations = ref<any[]>([]);
const expanded = ref<any[]>([]);

const handleLogout = () => {
  axios.defaults.headers.Authorization = "";

  localStorage.removeItem("token");

  appStore.user.token = "";
  appStore.isLoggedIn = false;

  router.push("/");
};

const getReservations = () => {
  loading.value = true;

  axios
    .get("/api/v1/reservations/")
    .then((response) => {
      reservations.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    })
    .finally(() => (loading.value = false));
};

onMounted(() => {
  getReservations();
});
</script>

<template>
  <v-container>
    <h1 class="text-h2 mb-4">My Account</h1>
    <v-btn class="mb-4 mx-auto" @click="handleLogout"> Log Out </v-btn>
    <v-data-table
      v-model:expanded="expanded"
      :headers="reservationHeaders"
      :items="reservations"
      item-value="id"
      show-expand
      single-expand
    >
      <template #top>
        <v-toolbar title="Reservations" density="compact" color="primary" />
      </template>
      <template #expanded-row="{ columns, item: order }">
        <tr>
          <td :colspan="columns.length">
            <v-list>
              <template v-for="(item, i) in order.items" :key="item.item.id">
                <v-list-item
                  :title="item.item.title"
                  :subtitle="item.item.author"
                />
                <v-divider v-if="i < order.items.length - 1" />
              </template>
            </v-list>
          </td>
        </tr>
      </template>
    </v-data-table>
  </v-container>
</template>
