import { filesApi, filesModel } from '@/entities/files'
import { useToggle } from '@vueuse/core'
import type { FileMeta } from 'shared-types'

export function useModel() {
    const filesStore = filesModel.filesStore()
    const [isDeleting, setDeleting] = useToggle()

    async function deleteFile(id: number) {
        setDeleting()
        const { status } = await filesApi.deleteFile(id)
        setDeleting()

        if (status === 'ok') {
            filesStore.removeFile(id)
        }

        return status
    }

 
    async function downloadFile(file: FileMeta) {
        const data = await $fetch(`/api/files?id=${file.id}`, {responseType: 'blob'})
        const a = document.createElement("a");
        const url = window.URL.createObjectURL(data as Blob);
        a.href = url;
        a.download = `${file.name}.${file.ext}`
        a.click();
    }

    return {
        deleteFile,
        downloadFile,
        isDeleting,
    }
}
