"""File Exceptions"""
from .base import NotFoundException, ConflictException, BadRequestException
from .constants import ExceptionConstants


class FileNotFoundException(NotFoundException):
    """File not found exception"""
    default_detail = ExceptionConstants.FILE_NOT_FOUND


class FileUrlExistsException(ConflictException):
    """File URL exists exception"""
    default_detail = ExceptionConstants.FILE_URL_EXISTS


class InvalidFileTypeException(BadRequestException):
    """Invalid file type exception"""
    default_detail = ExceptionConstants.INVALID_FILE_TYPE


class FileTooLargeException(BadRequestException):
    """File too large exception"""
    default_detail = ExceptionConstants.FILE_TOO_LARGE
