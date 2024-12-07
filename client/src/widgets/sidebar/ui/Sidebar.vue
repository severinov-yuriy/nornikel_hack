<script setup lang="ts">
import { FileList, UploadFiles } from '@/features/files'
</script>
<template>
    <div class="flex w-full flex-col items-start gap-4">
        <UploadFiles />
        <FileList />
    </div>
</template>

<style scoped></style>
