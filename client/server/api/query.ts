import { AnswerResponse } from '~/shared-types'

export default defineEventHandler(async (event) => {
    const body = await readBody(event)

    if (!body.query) {
        return createError({
            statusCode: 400,
            statusMessage: 'Invalid query',
        })
    }

    try {
        const response = await $fetch<AnswerResponse>(`${process.env.API_URL}/query/`, {
            method: 'post',
            body: JSON.stringify(body),
        })

        return response
    } catch (e) {
        return createError({
            message: 'Something went wrong...',
        })
    }
})
