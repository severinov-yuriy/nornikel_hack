import { answerApi } from '@/entities/answer'
import type { AnswerResponse } from 'shared-types'

export function useModel() {
    const searchTerm = ref('')
    const currentAnswer = ref<AnswerResponse>()
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

    const isFetching = ref(false)

    async function getData() {
        isFetching.value = true

        const answer = await answerApi.getAnswer(searchTerm.value)

        isFetching.value = false

        if (!answer) {
            return setError({
                title: 'Упс!',
                message: 'Что-то пошло не так...',
            })
        }

        searchTerm.value = ''
        currentAnswer.value = answer
        setError(null)
    }

    return {
        searchTerm,
        getData,
        currentAnswer,
        isFetching,
        error,
        setError,
    }
}
