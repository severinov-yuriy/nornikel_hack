import files from './files.json'

export default defineEventHandler(async (event) => {
    try {
        // const response = await $fetch(`${process.env.API_URL}/files`)

        // return response

        return files
    } catch (e) {
        return createError({
            message: 'Something went wrong...',
        })
    }
})
