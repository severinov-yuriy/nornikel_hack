<script setup lang="ts">
import { ThemeToggle } from '@/features/theme-toggle'
</script>

<template>
    <header
        class="flex min-h-16 w-full items-center justify-between border-b border-gray-300 p-4 dark:border-gray-600"
    >
        <div>
            <ThemeToggle />
        </div>
    </header>
</template>

<style scoped></style>
