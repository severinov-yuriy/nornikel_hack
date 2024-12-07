<script setup lang="ts">
import { useModel } from '../model'
import AnswerContent from './AnswerContent.vue'

const { searchTerm, answerFetching, currentAnswer, getData, error, setError } = useModel()
</script>
<template>
    <div class="flex w-full flex-col gap-6">
        <form
            @submit.prevent="getData"
            class="flex w-full gap-2"
        >
            <UInput
                v-model="searchTerm"
                icon="i-heroicons-magnifying-glass-20-solid"
                size="xl"
                placeholder="Ввод..."
                :loading="answerFetching"
                class="flex-1"
            />
            <UButton
                label="Search"
                type="submit"
                size="xl"
                class="min-w-24 text-center"
                :loading="answerFetching"
            />
        </form>

        <AnswerContent
            :content="currentAnswer"
            v-if="currentAnswer"
        />
        <UAlert
            v-if="error"
            :title="error.title"
            :description="error.message"
            color="rose"
            variant="subtle"
            :close-button="{
                icon: 'i-heroicons-x-mark-20-solid',
                color: 'white',
                variant: 'link',
                padded: false,
            }"
            @close="setError(null)"
        />
    </div>
</template>

<style scoped></style>
