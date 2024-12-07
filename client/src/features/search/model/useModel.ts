import { answerApi, answerModel } from '@/entities/answer'
import { useToggle } from '@vueuse/core'
import type { AnswerResponse } from 'shared-types'

export function useModel() {
    const answerStore = answerModel.answerStore()
    const searchTerm = ref('')
    const error = ref<{ title: string; message: string } | null>(null)
    const [isFetching, toggleFetching] = useToggle()

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
        toggleFetching()

        const status = await answerStore.askQuestion(searchTerm.value)

        toggleFetching()

        if (status !== 'ok') {
            return setError({
                title: 'Упс!',
                message: 'Что-то пошло не так...',
            })
        }

        searchTerm.value = ''
        setError(null)
    }

    return {
        searchTerm,
        getData,
        isFetching,
        error,
        setError,
    }
}
