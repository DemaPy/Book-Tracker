<script setup lang="ts">
interface Post {
  id: number;
  title: string;
  body: string;
  userId: number;
}

defineProps<{ posts: Post[] }>();
</script>

<template>
  <h1>Posts</h1>
  <ul class="flex flex-col gap-2">
    <li
      class="rounded-md items-start text-left border px-4 py-2 border-gray-200 flex flex-col gap-2"
      v-for="post in posts"
    >
      <p class="capitalize">{{ post.title }}</p>
      <p>{{ post.body }}</p>
    </li>
  </ul>
</template>
