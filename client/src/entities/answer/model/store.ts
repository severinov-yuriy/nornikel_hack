import { defineStore } from 'pinia'
import type { Answer, FileMeta } from 'shared-types'
import { useToggle } from '@vueuse/core'
import { getAllFiles, getAnswer } from '../api'

export const answerStore = defineStore('answer', () => {
    const allFiles = ref<FileMeta[] | null>([
        {
            id: 1,
            name: 'Text',
            ext: 'txt',
        },
        {
            id: 2,
            name: 'Png',
            ext: 'png',
        },
        {
            id: 3,
            name: 'Pdf',
            ext: 'pdf',
        },
        {
            id: 4,
            name: 'Jpeg',
            ext: 'jpeg',
        },
        {
            id: 5,
            name: 'docx',
            ext: 'docx',
        },
    ])

    const currentAnswer = ref<Answer>()

    const [filesFetching, toggleFilesFetching] = useToggle()

    async function getFiles() {
        toggleFilesFetching()

        const response = await getAllFiles()

        toggleFilesFetching()

        if (response.status === 'error') {
            return
        }

        allFiles.value = response.payload.files
    }

    async function askQuestion(query: string) {
        const response = await getAnswer(query)

        if (response.status === 'ok') {
            currentAnswer.value = response.payload
        }

        return response.status
    }

    return {
        allFiles,
        filesFetching,
        getFiles,
        currentAnswer,
        askQuestion,
    }
})
