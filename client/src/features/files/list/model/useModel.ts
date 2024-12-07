import { filesApi, filesModel } from '@/entities/files'
import { useToggle } from '@vueuse/core'

export function useModel() {
    const filesStore = filesModel.filesStore()
    const [isDeleting, setDeleting] = useToggle()

    async function deleteFile(id: number) {
        setDeleting()
        const { status } = await filesApi.deleteFile(id)
        setDeleting()

        if (status === 'ok') {
            await filesStore.getFiles()
        }

        return status
    }

    async function downloadFile(id: number) {
        window.open(`/api/files?id=${id}`)
    }
    return {
        deleteFile,
        downloadFile,
        isDeleting,
    }
}
