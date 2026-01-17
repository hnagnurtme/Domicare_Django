import logging

from django.utils.deprecation import MiddlewareMixin

from repositories.user_repository import UserRepository
from services.jwt_service import JwtService

logger = logging.getLogger(__name__)

class JwtAuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.jwt_service = JwtService()
        self.user_repo = UserRepository()

    def process_request(self, request):
        public_paths = ['/login', '/register', '/refresh-token', '/verify-email']
        if any(request.path.startswith(path) for path in public_paths):
            return None

        # Get token from Authorization header
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header.startswith('Bearer '):
            return None

        token = auth_header[7:]  # Remove 'Bearer ' prefix

        try:
            # Decode token
            payload = self.jwt_service.decode_token(token)
            email = payload.get('email')

            # Load user
            user = self.user_repo.find_by_email(email)
            if user:
                request.user = user
                request.email = email
                logger.debug(f"[JWT] Authenticated user: {email}")

        except Exception as e:
            logger.warning(f"[JWT] Authentication failed: {str(e)}")

        return None