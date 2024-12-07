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
        class="flex h-full flex-1 flex-col justify-center"
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

        <div
            class="flex h-full w-full flex-1 flex-col justify-between gap-4"
            v-else
        >
            <ul class="flex w-full flex-col gap-2 max-h-[350px] overflow-auto">
                <li
                    v-for="file in filesData"
                    class="border-b py-2 text-xs"
                >
                    <div class="flex items-center justify-between">
                        <strong class="flex-1">Имя файла:</strong>
                        <span class="flex-1 text-right">{{ file.name }}</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <strong class="flex-1">Тип: </strong>
                        <span class="flex-1 text-right"> {{ file.type }}</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <strong class="flex-1">Размер:</strong>
                        <span class="flex-1 text-right"> {{ file.size }} bytes</span>
                    </div>
                </li>
            </ul>

            <div class="flex gap-4 justify-end">
                <UButton
                    label="Загрузить"
                    type="submit"
                    color="green"
                    :loading="isUploading"
                />

                <UButton
                    label="Сбросить"
                    color="red"
                    @click="filesData = []"
                />
            </div>
        </div>
    </form>

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
