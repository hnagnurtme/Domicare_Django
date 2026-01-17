from rest_framework.response import Response
from rest_framework import status as http_status

class RestResponse:
    @staticmethod
    def success(data=None, message="Success", status=http_status.HTTP_200_OK):
        """
        Format success response
        """
        return Response({
            'status': status,
            'error': None,
            'message': message,
            'data': data
        }, status=status)

    @staticmethod
    def error(message, error_code="error", status=http_status.HTTP_400_BAD_REQUEST):
        """
        Format error response
        """
        return Response({
            'status': status,
            'error': error_code,
            'message': message,
            'data': None
        }, status=status)