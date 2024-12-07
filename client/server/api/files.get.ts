import files from './files.json'

export default defineEventHandler(async (event) => {
    if (process.dev) {
        return files
    }
    try {
        const response = await $fetch(`${process.env.API_URL}/files`)

        return response
    } catch (e) {
        return createError({
            message: 'Something went wrong...',
        })
    }
})
