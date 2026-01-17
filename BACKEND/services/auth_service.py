import logging

from dtos.auth.login_request import LoginRequest
from dtos.auth.login_response import LoginResponse
from exceptions.auth_exceptions import InvalidEmailOrPassword, EmailNotConfirmedException
from exceptions.user_exceptions import UserNotFoundException
from mappers.user_mapper import UserMapper
from repositories.token_repository import TokenRepository
from repositories.user_repository import UserRepository
from services.jwt_service import JwtService

logger = logging.getLogger(__name__)

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.token_repo = TokenRepository()
        self.jwt_service = JwtService()

    def login(self, login_request: LoginRequest) -> LoginResponse:
        email = login_request.email
        password = login_request.password
        logger.info(f"[JWT] Login attempt for email: {email}")

        try:
            # Find user
            user = self.user_repo.find_by_email(email)
            if not user:
                raise InvalidEmailOrPassword("Email chưa được đăng ký hoặc mật khẩu sai.")

            # Verify password
            if not user.check_password(password):
                raise InvalidEmailOrPassword("Email chưa được đăng ký hoặc mật khẩu sai.")

            # Check if email is confirmed
            if not user.is_email_confirmed:
                raise EmailNotConfirmedException("Email chưa được xác thực.")

            # Update user active status
            user.is_active = True
            self.user_repo.save(user)

            # Generate tokens
            access_token = self.jwt_service.create_access_token(user.email)
            refresh_token = self.jwt_service.create_refresh_token(user.email)

            # Response
            user_dto = UserMapper.to_dto(user)
            login_response = LoginResponse(
                access_token=access_token,
                refresh_token=refresh_token,
                user=user_dto
            )

            logger.info(f"[JWT] Login successful for email: {email}")
            return login_response

        except (InvalidEmailOrPassword, EmailNotConfirmedException) as e:
            logger.info(f"[JWT] Login failed from email: {email}. Reason: {str(e)}")
            raise e
        except Exception as e:
            logger.error(f"[JWT] Unexpected error during login for email: {email}. Reason: {str(e)}")
            raise e

    def logout(self, email: str):
        logger.info("[JWT] Logout attempt")

        user = self.user_repo.find_by_email(email)
        if not user:
            logger.warning("[JWT] Logout failed - no user found")
            raise UserNotFoundException("Không tìm thấy người dùng")

        self.token_repo.delete_by_user_id(user.id)
        logger.info(f"[JWT] User {user.email} logged out and tokens cleared")