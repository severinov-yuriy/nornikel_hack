<script setup lang="ts">
import { answerModel } from '@/entities/answer'
import { FileList } from '@/features/files'
const { allFiles } = storeToRefs(answerModel.answerStore())
</script>
<template>
    <div class="w-full">
        <FileList
            :files="allFiles"
            v-if="allFiles"
        />
    </div>
</template>

<style scoped></style>
