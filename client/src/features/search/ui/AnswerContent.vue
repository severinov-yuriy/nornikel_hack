<script setup lang="ts">
import type { Answer } from 'shared-types'

const { content } = defineProps<{
    content: Answer
}>()

const paragraphs = computed(() => content.answer.split(/\n/).filter((str) => str.length))
</script>
<template>
    <section class="flex w-full flex-col gap-6 py-6">
        <h2 class="text-2xl font-semibold">{{ content.query }}</h2>

        <UDivider />

        <UContainer
            as="section"
            class="flex w-full flex-col gap-1 rounded-lg bg-gray-200 py-4 dark:bg-slate-600"
        >
            <p
                class="whitespace-break-spaces leading-7"
                v-for="p in paragraphs"
            >
                {{ p }}
            </p>
        </UContainer>
    </section>
</template>

<style scoped></style>
