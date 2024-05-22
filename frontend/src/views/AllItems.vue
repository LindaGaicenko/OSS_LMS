<template>
  <v-container>
    <v-row class="pa-3">
      <v-text-field
        v-model="filters.search"
        label="Search"
        compact
        hide-details
      />
    </v-row>
    <v-row>
      <v-col cols="12" sm="4">
        <Filter v-model="filters" />
      </v-col>
      <v-col cols="12" sm="8">
        <v-progress-linear
          :active="loading"
          color="primary"
          height="8"
          indeterminate
          rounded
        />
        <v-row>
          <v-col
            v-if="items.length"
            v-for="item in items"
            cols="12"
            sm="6"
            md="4"
            lg="4"
          >
            <v-card
              class="h-100 position-relative"
              @click="goToItem(item.get_absolute_url)"
            >
              <v-img
                v-if="item.get_thumbnail"
                :src="item.get_thumbnail"
                cover
                class="h-100"
              />
              <div
                class="card-desc position-absolute bottom-0 w-100 pa-4 bg-white"
              >
                <h3 class="text-no-wrap">{{ item.title }}</h3>
                <h5>{{ item.author }}</h5>
                <h5 class="text-secondary text-capitalize">{{ item.type }}</h5>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
import { onMounted, ref, watch } from "vue";
import axios from "axios";
import _ from "lodash";
import router from "@/router";
import Filter from "@/components/Items/Filter.vue";

const loading = ref(false);
const items = ref<any[]>([]);
const filters = ref({
  search: "",
  order: "",
  types: [],
  authors: [],
  publishers: [],
  date: {
    from: "",
    to: "",
  },
});

const getItems = () => {
  loading.value = true;

  const { order, search, types, authors, date } = filters.value;

  const params = [];

  if (order) params.push(`ordering=${order}`);
  if (search) params.push(`search=${search}`);
  if (types.length) {
    types.forEach((type) => {
      params.push(`type=${type}`);
    });
  }
  if (authors.length) params.push(`author__in=${authors.toString()}`);
  if (date.from) params.push(`from_date=${date.from}`);
  if (date.from) params.push(`to_date=${date.from}`);

  const requestQuery = "?" + params.join("&") || "";

  axios
    .get(`/api/v1/items/${requestQuery}`)
    .then(({ data }) => {
      items.value = data;
    })
    .catch((error) => {
      console.log(error);
    })
    .finally(() => (loading.value = false));
};

const goToItem = (slug: string) => {
  router.push(slug);
};

watch(
  filters.value,
  _.debounce(() => {
    getItems();
  }, 1000)
);

onMounted(() => {
  getItems();
});
</script>
