export type AnswerResponse = BaseResponse<Answer>

export type GetFilesResponse = BaseResponse<{
    total: number
    files: FileMeta[]
}>

export type Answer = {
    query: string
    response: string
    files: FileMeta[]
}

export type FileMeta = {
    id: number
    name: string
    ext: 'txt' | 'docx' | 'pdf' | 'jpeg' | 'png'
}

export type ErrorResponse = {
    status: 'error'
    errorCode: string
    errorMessage: string
}

export type BaseResponse<T> =
    | ErrorResponse
    | {
          status: 'ok'
          payload: T
      }
