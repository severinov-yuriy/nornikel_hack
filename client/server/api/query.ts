import data from './data.json'

export default defineEventHandler((event) => {
    const { q } = getQuery(event)
    return {
        ...data,
        query: q,
    }
})
