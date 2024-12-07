import { answerApi } from '@/entities/answer'
import { filesModel } from '@/entities/files'
import { useToggle } from '@vueuse/core'
import type { Answer } from 'shared-types'

export function useModel() {

    const currentAnswer = ref<Answer>()

    const [answerFetching, toggleAnswerFetching] = useToggle()

    const filesStore = filesModel.filesStore()

    const searchTerm = ref('')
    const error = ref<{ title: string; message: string } | null>(null)

    function setError(payload: { title: string; message: string } | null) {
        if (!payload) {
            error.value = null
            return
        }
        error.value = {
            title: payload.title,
            message: payload.message,
        }
    }

    async function getData() {
        if(!searchTerm.value.length) return
        
        toggleAnswerFetching()

        const res = await answerApi.getAnswer(searchTerm.value)

        toggleAnswerFetching()

        if (res.status !== 'ok') {
            return setError({
                title: 'Упс!',
                message: 'Что-то пошло не так...',
            })
        }

        if(res.payload) {
            const {files} = res.payload

            files && filesStore.setFiles(files)
            currentAnswer.value = res.payload
        }

        searchTerm.value = ''
        setError(null)
    }

    return {
        currentAnswer,
        searchTerm,
        getData,
        answerFetching,
        error,
        setError,
    }
}
