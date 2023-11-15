<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-text-field
          :loading="loading"
          label="Search"
          compact
          prepend-icon="mdi-magnify"
          @update:modelValue="handleSearch"
        />
      </v-col>
      <v-progress-linear
        :active="loading"
        color="primary"
        height="8"
        indeterminate
        rounded
      />
      <v-col
        v-if="books.length"
        v-for="book in books"
        cols="12"
        sm="6"
        md="4"
      >
        <v-card
          class="h-100"
          @click="goToBook(book.get_absolute_url)"
        >
          <v-img
            v-if="book.get_thumbnail"
            :src="book.get_thumbnail"
            cover
            class="h-75"
          />
          <v-card-title>{{ book.title }}</v-card-title>
          <v-card-subtitle>{{ book.author }}</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
  import { onMounted, ref } from 'vue'
  import axios from 'axios'
  import { debounce } from 'lodash'
  import router from '@/router'

  const loading = ref(false)
  const books = ref<any[]>([])

  const getBooks = (query = '') => {
    loading.value = true
    axios
      .post('/api/v1/books/search/', { query: query })
      .then(({ data }) => {
        books.value = data
      })
      .catch((error) => {
        console.log(error)
      })
      .finally(() => (loading.value = false))
  }

  const handleSearch = debounce((query: string) => getBooks(query), 500)

  const goToBook = (slug: string) => {
    router.push(slug)
  }

  onMounted(() => {
    getBooks()
  })
</script>
