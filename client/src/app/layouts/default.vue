<script setup lang="ts">
import { ThemeToggle } from '@/features/theme-toggle'
import Sidebar from '@/widgets/sidebar/ui/Sidebar.vue'
</script>

<template>
    <div class="relative flex min-h-full bg-white dark:bg-slate-700">
        <div class="min-w-[350px] border">
            <div class="sticky top-0 flex w-full flex-col px-4 py-6">
                <div class="w-full border-b pb-5">
                    <ThemeToggle />
                </div>

                <div class="w-full pt-5">
                    <Sidebar />
                </div>
            </div>
        </div>
        <div class="flex w-full flex-col items-center py-6">
            <slot />
        </div>
    </div>
    <UNotifications />
</template>

<style scoped></style>
