<script setup lang="ts">
import { onBeforeMount, ref } from "vue";
import axios from "axios";

const value = defineModel<any>();
const emit = defineEmits(["update"]);

const listLimit = 5;

const orderOptions = [
  { code: "author", label: "Author Asc" },
  { code: "-author", label: "Author Desc" },
  { code: "title", label: "Title Asc" },
  { code: "-title", label: "Title Desc" },
  { code: "publisher", label: "Publisher Asc" },
  { code: "-publisher", label: "Publisher Desc" },
];

const types = [
  { code: "book", label: "Book" },
  { code: "article", label: "Article" },
  { code: "document", label: "Document" },
  { code: "audiobook", label: "Audiobook" },
  { code: "audio", label: "Audio" },
  { code: "video", label: "Video" },
  { code: "podcast", label: "Podcast" },
];
const typeShowMore = ref(false);

const authors = ref<string[]>([]);
const authorShowMore = ref(false);

const publishers = ref<string[]>([]);
const publisherShowMore = ref(false);

const fetchOptions = () => {
  axios
    .get("/api/v1/items/filter")
    .then(({ data }) => {
      authors.value = data.authors;
      publishers.value = data.publishers;
    })
    .catch((error) => {
      console.log(error);
    });
};

onBeforeMount(async () => {
  fetchOptions();
});
</script>

<template>
  <v-card>
    <v-card-title class="cursor-pointer py-3"> Filter & Sort </v-card-title>
    <v-container class="bg-white pa-6 rounded h-80 overflow-y-auto">
      <v-row class="py-1">
        <v-select
          v-model="value.order"
          :items="orderOptions"
          label="Sort By"
          item-value="code"
          item-title="label"
          hide-details
        />
      </v-row>
      <v-row class="d-flex flex-column py-1">
        <h5 class="text-primary">Item Type</h5>
        <v-checkbox
          v-model="value.types"
          v-for="(type, index) in types"
          v-show="typeShowMore || index < listLimit"
          :label="type.label"
          :value="type.code"
          color="primary"
          density="compact"
          hide-details
        />
        <v-btn
          v-if="types.length > listLimit"
          size="small"
          variant="text"
          @click="typeShowMore = !typeShowMore"
        >
          {{ typeShowMore ? "Show less" : "Show more" }}
        </v-btn>
      </v-row>
      <v-row v-if="authors.length" class="d-flex flex-column py-1">
        <h5 class="text-primary">Author</h5>
        <v-checkbox
          v-model="value.authors"
          v-for="(author, index) in authors"
          v-show="authorShowMore || index < listLimit"
          :label="author"
          :value="author"
          color="primary"
          density="compact"
          hide-details
        />
        <v-btn
          v-if="authors.length > listLimit"
          size="small"
          variant="text"
          @click="authorShowMore = !authorShowMore"
        >
          {{ authorShowMore ? "Show less" : "Show more" }}
        </v-btn>
      </v-row>
      <v-row v-if="publishers.length" class="d-flex flex-column py-1">
        <h5 class="text-primary">Publisher</h5>
        <v-checkbox
          v-model="value.publishers"
          v-for="(publisher, index) in publishers"
          v-show="publisherShowMore || index < listLimit"
          :label="publisher"
          :value="publisher"
          color="primary"
          density="compact"
          hide-details
        />
        <v-btn
          v-if="publishers.length > listLimit"
          size="small"
          variant="text"
          @click="publisherShowMore = !publisherShowMore"
        >
          {{ publisherShowMore ? "Show less" : "Show more" }}
        </v-btn>
      </v-row>
      <v-row class="d-flex flex-column py-1">
        <h5 class="text-primary">Release Date</h5>
        <v-date-input v-model="value.date.from" label="From" :rounded="4" />
        <v-date-input v-model="value.date.from" label="To" :rounded="4" />
      </v-row>
    </v-container>
  </v-card>
</template>
