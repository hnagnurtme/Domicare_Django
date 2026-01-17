"""Category Exceptions"""
from .base import NotFoundException, ConflictException, BadRequestException
from .constants import ExceptionConstants


class CategoryNotFoundException(NotFoundException):
    """Category not found exception"""
    default_detail = ExceptionConstants.CATEGORY_NOT_FOUND


class CategoryNameExistsException(ConflictException):
    """Category name exists exception"""
    default_detail = ExceptionConstants.CATEGORY_NAME_EXISTS


class CategoryHasProductsException(BadRequestException):
    """Category has products exception"""
    default_detail = ExceptionConstants.CATEGORY_HAS_PRODUCTS
