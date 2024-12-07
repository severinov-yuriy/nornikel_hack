export default defineEventHandler(async (event) => {
    const body = await readBody(event)

    console.log(body)
  
    try {
        const response = await $fetch(`${process.env.API_URL}/upload/`, {
            method: 'post',
            body,
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        })

        return response
    } catch (e) {
        return createError({
            message: 'Something went wrong...',
        })
    }
})
