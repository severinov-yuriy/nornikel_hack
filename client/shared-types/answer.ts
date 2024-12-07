import type { FileMeta } from './files'

export type AnswerResponse = BaseResponse<Answer>

export type Answer = {
    query: string
    answer: string
    files: FileMeta[]
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
          payload: T | undefined
      }
