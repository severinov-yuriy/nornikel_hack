<script setup lang="ts">
const colorMode = useColorMode()

const isDark = computed({
    get() {
        return colorMode.value === 'dark'
    },
    set() {
        colorMode.preference = colorMode.value === 'dark' ? 'light' : 'dark'
    },
})
</script>
<template>
    <UToggle
        size="lg"
        v-model="isDark"
        on-icon="i-heroicons-sun"
        off-icon="i-heroicons-moon"
    />
</template>

<style scoped></style>
