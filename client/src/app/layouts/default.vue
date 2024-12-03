<script setup lang="ts">
import { VHeader } from '@/widgets/header'
</script>

<template>
    <div class="flex min-h-[100vh] flex-col bg-slate-100 dark:bg-slate-900">
        <VHeader />
        <div class="flex flex-col px-4 py-6">
            <slot />
        </div>
    </div>
</template>

<style scoped></style>
