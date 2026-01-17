import logging

from pydantic import ValidationError
from rest_framework.decorators import api_view
from rest_framework.request import Request

from dtos.auth.login_request import LoginRequest
from services.auth_service import AuthService
from utils.rest_response import RestResponse
from services.jwt_service import JwtService
from rest_framework import status as http_status

auth_service = AuthService()
logger = logging.getLogger(__name__)

@api_view(['POST'])
def login(request: Request):
    try:
        login_request = LoginRequest(**request.data)
        login_response = auth_service.login(login_request)

        return RestResponse.success(
            data={
                'access_token': login_response.access_token,
                'refresh_token': login_response.refresh_token,
                'user': login_response.user.model_dump(by_alias=True, exclude={'password'})
            }
        )
    except ValidationError as e:
        logger.warning(f"[Auth] Validation error during login: {str(e)}")
        raise
    except Exception as e:
        logger.warning(f"[Auth] Exception during login: {str(e)}")
        raise

@api_view(['POST'])
def logout(request: Request):
    try:
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return RestResponse.error(message="Missing or invalid authorization header", status=http_status.HTTP_401_UNAUTHORIZED)
        
        token = auth_header.replace('Bearer ', '')
        
        # Decode token để lấy email
        jwt_service = JwtService()
        payload = jwt_service.decode_token(token)
        email = payload.get('email')
        
        if email: 
            auth_service.logout(email)
        
        return RestResponse.success(message="Logged out successfully")
    except Exception as e:
        logger.error(f"[Auth] Logout error: {e}")
        return RestResponse.error(message="Logout failed", status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)
