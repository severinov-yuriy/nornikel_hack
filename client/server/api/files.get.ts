import files from './files.json'

export default defineEventHandler(async (event) => {
    const query = getQuery(event)
    if (process.dev) {
        return files
    }
    try {
        const response = await $fetch(`${process.env.API_URL}/files/`, {
            query,
        })
        return response
    } catch (e) {
        return createError({
            message: 'Something went wrong...',
        })
    }
})
