<script lang="ts" setup>
  import { onMounted, ref } from 'vue'
  import axios from 'axios'
  import { useAppStore } from '@/store/app'
  import { useCartStore } from '@/store/cart'

  const props = defineProps({
    categorySlug: {
      type: String,
      required: true
    },
    bookSlug: {
      type: String,
      required: true
    }
  })

  const appStore = useAppStore()
  const cartStore = useCartStore()

  const loading = ref(false)
  const book = ref<any>({})

  const getBook = () => {
    loading.value = true
    axios
      .get(`/api/v1/books/${props.categorySlug}/${props.bookSlug}/`)
      .then(({ data }) => {
        book.value = data
      })
      .finally(() => {
        loading.value = false
      })
  }

  const addToCart = () => {
    if (!cartStore.items.includes(book.value)) {
      cartStore.items.push(book.value)

      localStorage.setItem('cart', JSON.stringify(cartStore.items))
    }
  }

  onMounted(() => {
    getBook()
  })
</script>

<template>
  <v-container>
    <v-row>
      <v-col
        cols="12"
        sm="5"
      >
        <v-img
          :src="book.get_image"
          cover
          class="w-100"
        />
      </v-col>
      <v-col>
        <h1 class="text-h1 mb-4">{{ book.title }}</h1>
        <h4 class="text-h4 mb-4">{{ book.author }}</h4>
        <v-divider class="my-4" />
        <span>{{ book.description }}</span>
        <v-divider class="my-4" />
        <v-row>
          <v-col cols="auto">
            <span>
              Book is
              <span :class="`text-${book.available ? 'success' : 'error'}`">
                {{ book.available ? 'available' : 'unavailable' }}
              </span>
              .
            </span>
          </v-col>
          <v-spacer />
          <v-col
            v-if="appStore.isLoggedIn"
            cols="auto"
          >
            <v-btn
              variant="text"
              :disabled="!book.available"
              @click="addToCart"
            >
              Add to Cart
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>
