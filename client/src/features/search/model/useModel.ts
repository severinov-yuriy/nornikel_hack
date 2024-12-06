import { answerApi } from '@/entities/answer'

export function useModel() {
    const searchTerm = ref('')
    const currentAnswer = ref<answerApi.AnswerResponse>()

    const isFetching = ref(false)

    async function getData() {
        isFetching.value = true

        const answer = await answerApi.getAnswer(searchTerm.value)

        isFetching.value = false

        if (answer) {
            searchTerm.value = ''
            currentAnswer.value = answer
        }
    }

    return {
        searchTerm,
        getData,
        currentAnswer,
        isFetching,
    }
}
