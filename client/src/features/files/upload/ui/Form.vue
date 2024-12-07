<script setup lang="ts">
import { useDropZone } from '@vueuse/core'
import { useModel } from '../model'

const { filesData, onSubmit, onDrop, onFileChanged, isUploading, uploadStatus } = useModel()

const dropZoneRef = ref<HTMLElement>()

const { isOverDropZone } = useDropZone(dropZoneRef, {
    onDrop,
    multiple: true,
})
</script>

<template>
    <form
        class="it flex flex-col justify-center"
        @submit.prevent="onSubmit"
        v-if="uploadStatus === 'PENDING'"
    >
        <label
            v-if="!filesData.length"
            ref="dropZoneRef"
            :class="[
                'flex',
                'items-center',
                'justify-center',
                'text-center',
                'min-h-[200px]',
                'border-4',
                'border-dotted',
                'border-blue-300',
                { 'border-blue-600': isOverDropZone },
            ]"
        >
            <input
                type="file"
                multiple
                class="hidden"
                @change="onFileChanged"
            />
            Кликните по области <br />
            или
            <br />
            Перетащите файлы для загрузки
        </label>

        <div class="flex w-full flex-col gap-4">
            <ul class="flex w-full flex-col gap-2">
                <li
                    v-for="file in filesData"
                    class="border-b py-2 text-xs"
                >
                    <div class="flex items-center justify-between">
                        <strong>Имя файла:</strong>
                        <span class="text-right">{{ file.name }}</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <strong>Тип: </strong>
                        <span class="text-right"> {{ file.type }}</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <strong>Размер:</strong>
                        <span class="text-right"> {{ file.size }}</span>
                    </div>
                </li>
            </ul>

            <UButton
                v-if="filesData.length"
                label="Загрузить"
                type="submit"
                :loading="isUploading"
            />
        </div>
    </form>

    <UAlert
        v-if="uploadStatus === 'ERROR'"
        title="Ошибка"
        description="Попробуйте загрузить позже"
        variant="soft"
        color="red"
        @close="uploadStatus = 'PENDING'"
        :close-button="{
            icon: 'i-heroicons-x-mark-20-solid',
            color: 'white',
            variant: 'link',
            padded: false,
        }"
    />

    <UAlert
        v-if="uploadStatus === 'SUCCESS'"
        title="Успешно"
        description="Файлы загружены"
        color="green"
        variant="soft"
        @close="uploadStatus = 'PENDING'"
        :close-button="{
            icon: 'i-heroicons-x-mark-20-solid',
            color: 'white',
            variant: 'link',
            padded: false,
        }"
    />
</template>

<style scoped></style>
