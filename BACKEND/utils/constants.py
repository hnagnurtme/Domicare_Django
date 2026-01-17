"""Project Constants"""


class ProjectConstants:
    """
    Project-wide constants
    Matches ProjectConstants.java
    """
    
    # Pagination
    DEFAULT_PAGE_SIZE = 10
    MAX_PAGE_SIZE = 100
    
    # File upload
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
    ALLOWED_FILE_TYPES = ['application/pdf', 'application/msword']
    
    # JWT
    ACCESS_TOKEN_EXPIRY = 60 * 30  # 30 minutes in seconds
    REFRESH_TOKEN_EXPIRY = 60 * 60 * 24 * 7  # 7 days in seconds
    
    # Email
    EMAIL_CONFIRMATION_TOKEN_EXPIRY = 60 * 60 * 24  # 24 hours
    
    # Booking
    BOOKING_CANCEL_DEADLINE_HOURS = 24  # Can cancel 24h before start time
    
    # Rating
    MIN_RATING = 1
    MAX_RATING = 5
    
    # VNPay
    VNPAY_VERSION = "2.1.0"
    VNPAY_COMMAND = "pay"
    VNPAY_CURRENCY_CODE = "VND"
    VNPAY_LOCALE = "vn"
    
    # Roles
    ROLE_ADMIN = "ADMIN"
    ROLE_USER = "USER"
    ROLE_SALE = "SALE"
    
    # Default values
    DEFAULT_AVATAR = "https://res.cloudinary.com/domicare/image/upload/v1/default-avatar.png"
    SYSTEM_USER = "system"
