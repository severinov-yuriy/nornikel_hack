
export default defineEventHandler(async (event) => {
    const body = await readBody(event)

    if (process.dev) {
        return body
    }
    try {
        const response = await $fetch(`${process.env.API_URL}/files/${body.id}`, {
            method: 'delete',
            body,
            onRequest({request}) {
                console.log(request)
            }
        })

        return response
    } catch (e) {
        return createError({
            message: 'Something went wrong...',
        })
    }
})
