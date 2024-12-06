<script setup lang="ts">
import { useModel } from '../model'
import AnswerContent from './AnswerContent.vue'
const { searchTerm, currentAnswer, isFetching, getData } = useModel()
</script>
<template>
    <div class="w-full">
        <form @submit.prevent="getData">
            <UInput
                v-model="searchTerm"
                icon="i-heroicons-magnifying-glass-20-solid"
                size="xl"
                placeholder="Ввод..."
                :loading="isFetching"
            />
        </form>

        <AnswerContent
            :content="currentAnswer"
            v-if="currentAnswer"
        />
    </div>
</template>

<style scoped></style>
