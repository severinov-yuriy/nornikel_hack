import { AnswerResponse } from '~/shared-types'
import answer from './answer.json'


export default defineEventHandler(async (event) => {
    const body = await readBody(event)

    if(process.dev) {
        return {
            ...answer,
            query: body.query,
          }
    }

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

        console.log(response)

        return response
    } catch (e) {
        return createError({
            message: 'Something went wrong...',
        })
    }
})
