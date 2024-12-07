<script setup lang="ts">
import { ThemeToggle } from '@/features/theme-toggle'
import { VHeader } from '@/widgets/header'
import Sidebar from '@/widgets/sidebar/ui/Sidebar.vue'
</script>

<template>
    <div class="relative flex min-h-full bg-white dark:bg-slate-700">
        <div class="min-w-[250px] border">
            <div class="sticky top-0 flex w-full flex-col gap-10 px-4 py-6">
                <ThemeToggle />

                <Sidebar />
            </div>
        </div>
        <div class="flex w-full max-w-screen-lg flex-col py-6">
            <slot />
        </div>
    </div>
</template>

<style scoped></style>
