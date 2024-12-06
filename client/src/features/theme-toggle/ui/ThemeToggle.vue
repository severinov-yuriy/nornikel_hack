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
        off-icon="i-heroicons-sun"
        on-icon="i-heroicons-moon"
    />
</template>

<style scoped></style>
