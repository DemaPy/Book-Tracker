<script setup lang="ts">

interface ButtonProps {
    icon: any; // type for vue component?
    title: string;
    onClick: any; // type for vue handler (emit?)
}

defineProps<ButtonProps>()
</script>

<template>
    {{ title }}
</template>