<script setup lang="ts">
import { DocIcon, ImageIcon, PdfIcon } from '@/shared/icons'
import type { FileMeta } from 'shared-types'
import { useModel } from '../model'

const { deleteFile, downloadFile, isDeleting } = useModel()

const { file } = defineProps<{
    file: FileMeta
}>()

const icons = {
    docx: DocIcon,
    doc: DocIcon,
    jpeg: ImageIcon,
    pdf: PdfIcon,
    png: ImageIcon,
    txt: DocIcon,
}
</script>

<template>
    <li class="flex items-center gap-3 border-b">
        <UPopover
            class="h-full w-full transition-colors duration-150 ease-in hover:text-blue-400"
            :popper="{ placement: 'bottom' }"
            mode="hover"
        >
            <div class="flex w-full items-center gap-1">
                <div class="h-6 w-6">
                    <component :is="icons[file.ext]" />
                </div>
                <span class="inline-block w-full overflow-hidden text-ellipsis text-sm">{{
                    `${file.name}.${file.ext}`
                }}</span>
            </div>

            <template #panel>
                <div class="flex flex-col px-1 py-2 dark:bg-slate-700">
                    <UButton
                        label="Скачать"
                        size="xs"
                        variant="link"
                        icon="i-heroicons-arrow-down-tray"
                        :to="`/api/files/?id=${file.id}`" target="_blank"

                    />
                    <UButton
                        label="Удалить"
                        size="xs"
                        variant="link"
                        color="red"
                        icon="i-heroicons-trash"
                        @click="deleteFile(file.id)"
                        :loading="isDeleting"
                    />
                </div>
            </template>
        </UPopover>
    </li>
</template>

<style scoped></style>
