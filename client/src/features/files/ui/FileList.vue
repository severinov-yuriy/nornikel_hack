<script setup lang="ts">
import type { FileMeta } from 'shared-types'
import File from './File.vue'

const { files } = defineProps<{
    files: FileMeta[]
}>()
</script>

<template>
    <ul class="flex flex-col gap-1">
        <File
            v-for="file in files"
            :key="file.id"
            :file
        />
    </ul>
</template>

<style scoped></style>
