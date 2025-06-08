<script setup lang="ts">
interface BookListItem {
  id: string;
  title: string;
  author: string;
  read: boolean;
}
const props = defineProps<{ item: BookListItem}>();
console.log(props);

</script>

<template>
    {{ props }}
</template>
