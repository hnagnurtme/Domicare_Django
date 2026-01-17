"""Format Response Utility"""
from rest_framework.response import Response
from rest_framework import status
from typing import Any, Optional


class FormatRestResponse:
    """
    Format REST API responses
    Matches FormatRestResponse.java
    """
    
    @staticmethod
    def success(data: Any = None, message: str = "Success", status_code: int = status.HTTP_200_OK) -> Response:
        """Format success response"""
        response_data = {
            'success': True,
            'message': message,
            'data': data
        }
        return Response(response_data, status=status_code)
    
    @staticmethod
    def created(data: Any = None, message: str = "Created successfully") -> Response:
        """Format created response"""
        return FormatRestResponse.success(data, message, status.HTTP_201_CREATED)
    
    @staticmethod
    def error(message: str = "Error occurred", errors: Optional[dict] = None, status_code: int = status.HTTP_400_BAD_REQUEST) -> Response:
        """Format error response"""
        response_data = {
            'success': False,
            'message': message,
            'errors': errors
        }
        return Response(response_data, status=status_code)
    
    @staticmethod
    def paginated(data: list, total: int, page: int, page_size: int, message: str = "Success") -> Response:
        """Format paginated response"""
        response_data = {
            'success': True,
            'message': message,
            'data': data,
            'pagination': {
                'total': total,
                'page': page,
                'page_size': page_size,
                'total_pages': (total + page_size - 1) // page_size
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)
