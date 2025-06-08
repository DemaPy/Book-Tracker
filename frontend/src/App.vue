<script setup lang="ts">
import { ref } from "vue";
import PostList from "./components/PostsList.vue";

interface Post {
  id: number;
  title: string;
  body: string;
  userId: number;
}

const posts = ref<Post[]>([]);
fetch("https://jsonplaceholder.typicode.com/posts")
  .then((response) => response.json())
  .then((json) => (posts.value = json));
</script>

<template>
  <PostList :posts="posts" />
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
