"""User Exceptions"""
from .base import NotFoundException, ConflictException, BadRequestException
from .constants import ExceptionConstants


class UserNotFoundException(NotFoundException):
    """User not found exception"""
    def __init__(self, detail="Không tìm thấy người dùng."):
        super().__init__(detail=detail)


class EmailAlreadyExistsException(ConflictException):
    """Email already exists exception"""
    def __init__(self, detail="Email đã tồn tại."):
        super().__init__(detail=detail)


class PhoneAlreadyExistsException(ConflictException):
    """Phone already exists exception"""
    def __init__(self, detail="Số điện thoại đã tồn tại."):
        super().__init__(detail=detail)


class UserInactiveException(BadRequestException):
    """User inactive exception"""
    def __init__(self, detail="Người dùng không hoạt động."):
        super().__init__(detail=detail)


class UserDeletedException(BadRequestException):
    """User deleted exception"""
    def __init__(self, detail="Người dùng đã bị xóa."):
        super().__init__(detail=detail)
