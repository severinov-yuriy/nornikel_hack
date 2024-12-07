import { defineStore } from 'pinia'
import type { Answer } from 'shared-types'
import { useToggle } from '@vueuse/core'
import { getAnswer } from '../api'

export const answerStore = defineStore('answer', () => {
    const currentAnswer = ref<Answer>()

    const [answerFetching, toggleAnswerFetching] = useToggle()

    async function askQuestion(query: string) {
        toggleAnswerFetching()
        const response = await getAnswer(query)

        toggleAnswerFetching()

        if (response.status === 'ok') {
            currentAnswer.value = response.payload
        }

        return response.status
    }

    return {
        answerFetching,
        currentAnswer,
        askQuestion,
    }
})
