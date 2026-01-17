export interface SuccessResponse<dataType> {
  status: number
  error?: string
  message: string
  data: dataType
}

export interface FailResponse<dataType> {
  status?: number
  error?: string
  message?: string
  data?: dataType
}
export interface PaginationResponse {
  page?: number
  size?: number
  total?: number
  totalPages?: number
}
