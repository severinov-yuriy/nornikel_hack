<script setup lang="ts">
import { VHeader } from '@/widgets/header'
</script>

<template>
    <div class="relative flex min-h-full flex-col items-center bg-white dark:bg-slate-700">
        <div class="sticky top-0 z-50 w-full bg-inherit">
            <VHeader />
        </div>
        <div class="flex w-full max-w-screen-lg flex-col py-6">
            <slot />
        </div>
    </div>
</template>

<style scoped></style>
