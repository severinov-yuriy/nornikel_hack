import { answerModel } from '@/entities/answer'

export function useModel() {
    const answerStore = answerModel.answerStore()
    const { answerFetching, currentAnswer } = storeToRefs(answerStore)
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
        const status = await answerStore.askQuestion(searchTerm.value)

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
        currentAnswer,
        searchTerm,
        getData,
        answerFetching,
        error,
        setError,
    }
}
