import { defineStore } from 'pinia'
import type { FileMeta } from 'shared-types'
import { useToggle } from '@vueuse/core'
import { getAllFiles } from '../api'

export const filesStore = defineStore('files', () => {
    const allFiles = ref<FileMeta[] | null>([])
    const [filesFetching, toggleFilesFetching] = useToggle()

    async function getFiles() {
        toggleFilesFetching()

        const response = await getAllFiles()

        toggleFilesFetching()

        if (response.status === 'error') {
            return
        }

        if (response.payload?.files?.length) {
            allFiles.value = response.payload.files
        }
    }

    return {
        allFiles,
        filesFetching,
        getFiles,
    }
})
