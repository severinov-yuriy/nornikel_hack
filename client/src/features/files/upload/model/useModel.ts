import { filesApi, filesModel } from '@/entities/files'
import { useToggle } from '@vueuse/core'

export function useModel() {
    const toast = useToast()
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

        filesData.value.forEach((file) => formData.append(`files`, file, file.name))

        toggleUploading()

        try {
            const response = await filesApi.uploadFiles(formData)


            if (response.status === 'error') {
                toast.add({
                    color: 'red',
                    title: 'Ошибка',
                    description: 'Не удалось загрузить, попробуйте еще раз...',
                    timeout: 30000
                })
                return
            }

            await filesStore.getFiles()

            filesData.value = []
            uploadStatus.value = 'SUCCESS'
        } catch {
            toast.add({
                color: 'red',
                title: 'Ошибка',
                description: 'Не удалось загрузить, попробуйте еще раз...',
                timeout: 0
            })
        } finally {
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
