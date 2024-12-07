<script setup lang="ts">
import Form from './Form.vue'

const isOpen = ref(false)
</script>
<template>
    <UButton
        icon="i-heroicons-folder-plus"
        variant="soft"
        @click="isOpen = true"
    />
    <UModal v-model="isOpen">
        <UContainer class="flex min-h-[300px] min-w-[500px] flex-col justify-center p-6">
            <Form />
        </UContainer>
    </UModal>
</template>

<style scoped></style>
