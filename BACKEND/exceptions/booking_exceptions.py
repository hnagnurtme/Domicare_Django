"""Booking Exceptions"""
from .base import NotFoundException, BadRequestException
from .constants import ExceptionConstants


class BookingNotFoundException(NotFoundException):
    """Booking not found exception"""
    default_detail = ExceptionConstants.BOOKING_NOT_FOUND


class BookingAlreadyCancelledException(BadRequestException):
    """Booking already cancelled exception"""
    default_detail = ExceptionConstants.BOOKING_ALREADY_CANCELLED


class BookingCannotCancelException(BadRequestException):
    """Cannot cancel booking exception"""
    default_detail = ExceptionConstants.BOOKING_CANNOT_CANCEL


class InvalidBookingStatusException(BadRequestException):
    """Invalid booking status exception"""
    default_detail = ExceptionConstants.INVALID_BOOKING_STATUS
