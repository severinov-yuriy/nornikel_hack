import { AnswerResponse } from '~/shared-types'

export default defineEventHandler(async (event) => {
    const { q } = getQuery(event)

    if (!q) {
        return createError({
            statusCode: 400,
            statusMessage: 'Invalid query',
        })
    }

    try {
        const response = await $fetch<AnswerResponse>(`${process.env.API_URL}/api`, {
            query: {
                query: q,
            },
            onRequest({ request }) {
                console.log(request)
            },
        })

        return response
    } catch (e) {
        return createError({
            message: 'Something went wrong...',
        })
    }
})
