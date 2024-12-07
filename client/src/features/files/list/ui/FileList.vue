<script setup lang="ts">
import File from './File.vue'
import { filesModel } from '@/entities/files'

const filesStore = filesModel.filesStore()

onBeforeMount(() => filesStore.getFiles())
</script>

<template>
    <div class="flex w-full flex-col">
        <ul
            class="flex w-full flex-col gap-1"
            v-if="filesStore.allFiles?.length"
        >
            <File
                v-for="file in filesStore.allFiles"
                :key="file.id"
                :file
            />
        </ul>
        <div v-else>Файлы не найдены</div>
    </div>
</template>

<style scoped></style>
