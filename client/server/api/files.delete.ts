
export default defineEventHandler(async (event) => {
    const body = await readBody(event)

    if (process.dev) {
        return body
    }
    try {
        const response = await $fetch(`${process.env.API_URL}/files/`, {
            method: 'delete',
            body,
        })

        return response
    } catch (e) {
        return createError({
            message: 'Something went wrong...',
        })
    }
})
