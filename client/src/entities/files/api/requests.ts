import type { AllFilesPayload, BaseResponse } from 'shared-types'

export async function getAllFiles(): Promise<BaseResponse<AllFilesPayload>> {
    try {
        const response = await $fetch<AllFilesPayload>('/api/files')
        return {
            status: 'ok',
            payload: response,
        }
    } catch (e) {
        return {
            status: 'error',
            errorCode: '666',
            errorMessage: 'Something went wrong',
        }
    }
}

export async function uploadFiles(formData: FormData) {
    try {
        const response = await $fetch('/api/upload', {
            method: 'post',
            headers: {
                'Content-Type': 'multipart/form-data',
            },
            body: formData,
        })
        return response
    } catch (e) {
        return {
            status: 'error',
            errorCode: '666',
            errorMessage: 'Something went wrong',
        }
    }
}
