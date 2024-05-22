<script lang="ts" setup>
import { computed, onMounted, ref } from "vue";
import axios from "axios";
import moment from "moment";
import { useAppStore } from "@/store/app";
import { useCartStore } from "@/store/cart";
import FilePreview from "@/components/Items/FilePreview.vue";

const props = defineProps({
  categorySlug: {
    type: String,
    required: true,
  },
  itemSlug: {
    type: String,
    required: true,
  },
});

const appStore = useAppStore();
const cartStore = useCartStore();

const loading = ref(false);
const item = ref<any>({});
const showItem = ref(false);

const isDigital = computed(() => {
  return !!item.value?.get_file || !!item.value?.file_url;
});
const file = computed(() => {
  return isDigital && item.value?.is_external
    ? item.value?.file_url
    : item.value?.get_file;
});

const getItem = () => {
  loading.value = true;
  axios
    .get(`/api/v1/items/${props.categorySlug}/${props.itemSlug}/`)
    .then(({ data }) => {
      item.value = data;
    })
    .finally(() => {
      loading.value = false;
    });
};

const addToCart = () => {
  if (!cartStore.items.includes(item.value)) {
    cartStore.items.push(item.value);

    localStorage.setItem("cart", JSON.stringify(cartStore.items));
  }
};

onMounted(() => {
  getItem();
});
</script>

<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="4">
        <v-img :src="item.get_image" cover class="w-100" />
      </v-col>
      <v-col>
        <h3 class="text-h3 mb-4">{{ item.title }}</h3>
        <h4 class="text-h4 mb-4">{{ item.author }}</h4>
        <span class="text-subtitle-2 mb-4">{{ item.publisher }}</span>
        <br />
        <span class="text-subtitle-2 mb-4">
          {{ moment(item.publication_date).format("MMMM DD YYYY") }}
        </span>
        <v-divider class="my-4" />
        <span class="font-italic">{{ item.description }}</span>
        <v-divider class="my-4" />
        <v-row>
          <v-col cols="auto">
            <span v-if="!isDigital">
              Item is
              <span :class="`text-${item.available ? 'success' : 'error'}`">
                {{ item.available ? "available" : "unavailable" }}
              </span>
              .
            </span>
          </v-col>
          <v-spacer />
          <v-col v-if="appStore.isLoggedIn" cols="auto">
            <v-btn
              v-if="isDigital"
              variant="text"
              @click="showItem = !showItem"
            >
              {{ showItem ? "Hide" : "Show" }}
            </v-btn>
            <v-btn
              v-else
              variant="text"
              :disabled="!item.available"
              @click="addToCart"
            >
              Add to Cart
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="d-flex justify-center">
        <FilePreview
          v-if="file && showItem"
          :file="file"
          :thumbnail="item.get_image"
        />
      </v-col>
    </v-row>
  </v-container>
</template>
