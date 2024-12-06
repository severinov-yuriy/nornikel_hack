import type { AnswerResponse } from './types'

export async function getAnswer(query: string) {
    return $fetch<AnswerResponse>('/api/query', {
        query: {
            q: query,
        },
    })
}
