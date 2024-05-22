<script setup>
import { computed } from "vue";
import VuePdfEmbed from "vue-pdf-embed";
import AudioPlayer from "vue3-audio-player";
import { VideoPlayer } from "@videojs-player/vue";

const props = defineProps({
  file: String,
  thumbnail: String,
});

const type = computed(() => {
  return props.file.split(".").pop();
});
</script>

<template>
  <VuePdfEmbed
    v-if="type === 'pdf'"
    style="box-shadow: 0 2px 8px 4px rgba(0, 0, 0, 0.1)"
    annotation-layer
    text-layer
    :source="file"
  />
  <AudioPlayer
    v-if="type === 'mp3'"
    :option="{ src: file, coverImage: thumbnail }"
  />
  <VideoPlayer class="w-60" :src="file" controls />
</template>

<style>
@import "vue-pdf-embed/dist/style/index.css";
@import "vue-pdf-embed/dist/style/annotationLayer.css";
@import "vue-pdf-embed/dist/style/textLayer.css";
@import "vue3-audio-player/dist/style.css";
@import "video.js/dist/video-js.css";
</style>
