import type { AnswerResponse } from 'shared-types'

export async function getAnswer(query: string) {
    try {
        const response = await $fetch<AnswerResponse>('/api/query', {
            method: 'post',
            body: JSON.stringify({ query }),
            retry: false,
        })
        return response
    } catch (e) {
        return null
    }
}
