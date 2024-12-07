
export default defineEventHandler(async (event) => {
    const body = await readBody(event)
    const contentType = event.headers.get('content-type') ?? ''
  
    try {
        const response = await $fetch(`${process.env.API_URL}/upload/`, {
            method: 'post',
            body,
            headers: {
                'Content-type': contentType 
            },
        })

        return response
    } catch (e) {
        return createError({
            message: 'Something went wrong...',
        })
    }
})
