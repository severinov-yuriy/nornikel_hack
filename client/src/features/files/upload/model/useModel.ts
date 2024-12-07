import { filesApi, filesModel } from '@/entities/files'
import { useToggle } from '@vueuse/core'

export function useModel() {
    const filesStore = filesModel.filesStore()

    const filesData = ref<File[]>([])

    const [isUploading, toggleUploading] = useToggle(false)

    const uploadStatus = ref<'PENDING' | 'ERROR' | 'SUCCESS'>('PENDING')

    function onDrop(files: File[] | null) {
        filesData.value = []
        if (files) {
            filesData.value = files
        }
    }

    function onFileChanged($event: Event) {
        const target = $event.target as HTMLInputElement
        if (target && target.files) {
            filesData.value = Array.from(target.files)
        }
    }

    async function onSubmit() {
        const formData = new FormData()

        filesData.value.forEach((file, idx) => formData.append(`files[${idx}]`, file))

        toggleUploading()

        try {
            const response = await filesApi.uploadFiles(formData)

            console.log(response)

            if (response.status === 'error') {
                uploadStatus.value = 'ERROR'
                return
            }

            await filesStore.getFiles()

            uploadStatus.value = 'SUCCESS'
        } catch {
            uploadStatus.value = 'ERROR'
        } finally {
            filesData.value = []
            toggleUploading()
        }
    }

    return {
        filesData,
        onDrop,
        onFileChanged,
        onSubmit,
        isUploading,
        uploadStatus,
    }
}
