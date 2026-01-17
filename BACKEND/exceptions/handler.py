"""Global Exception Handler"""
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import Http404
import logging

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Custom exception handler for DRF
    Matches GlobalExceptionHandler.java
    """
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    # Log the exception
    logger.error(f"Exception: {exc.__class__.__name__}: {str(exc)}")

    # If response is None, it means DRF didn't handle it
    if response is None:
        if isinstance(exc, ValidationError):
            return Response({
                'error': 'Validation Error',
                'message': str(exc),
                'details': exc.message_dict if hasattr(exc, 'message_dict') else None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        elif isinstance(exc, Http404):
            return Response({
                'error': 'Not Found',
                'message': 'Resource not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        else:
            # Generic server error
            return Response({
                'error': 'Internal Server Error',
                'message': str(exc)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Customize DRF response format
    error_response = {
        'error': response.data.get('detail', 'Error'),
        'message': str(exc),
        'status_code': response.status_code
    }

    return Response(error_response, status=response.status_code)
