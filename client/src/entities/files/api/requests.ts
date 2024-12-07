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

export async function deleteFile(id: number): Promise<BaseResponse<AllFilesPayload>> {
    try {
        const response = await $fetch<AllFilesPayload>('/api/files', {
            method: 'DELETE',
            body: JSON.stringify({
                id,
            }),
        })
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

export async function uploadFiles(formData: FormData): Promise<BaseResponse<{}>> {
    try {
        const response = await $fetch('/api/upload', {
            method: 'post',
            headers: {
                'Content-Type': 'multipart/form-data',
            },
            body: formData,
        })
        return {
            status: 'ok',
            payload: undefined,
        }
    } catch (e) {
        return {
            status: 'error',
            errorCode: '666',
            errorMessage: 'Something went wrong',
        }
    }
}
