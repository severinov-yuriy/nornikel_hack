export type FileMeta = {
    id: number
    name: string
    ext: 'txt' | 'docx' | 'pdf' | 'jpeg' | 'png'
}

export type AllFilesPayload = {
    total: number
    files: FileMeta[]
}
