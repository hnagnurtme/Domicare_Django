"""Exception Constants"""


class ExceptionConstants:
    """Exception message constants"""
    
    # User exceptions
    USER_NOT_FOUND = "User not found"
    EMAIL_ALREADY_EXISTS = "Email already exists"
    PHONE_ALREADY_EXISTS = "Phone number already exists"
    USER_INACTIVE = "User account is inactive"
    USER_DELETED = "User account has been deleted"
    
    # Auth exceptions
    INVALID_CREDENTIALS = "Invalid email or password"
    EMAIL_NOT_CONFIRMED = "Email not confirmed"
    INVALID_TOKEN = "Invalid token"
    TOKEN_EXPIRED = "Token has expired"
    REFRESH_TOKEN_NOT_FOUND = "Refresh token not found"
    
    # Booking exceptions
    BOOKING_NOT_FOUND = "Booking not found"
    BOOKING_ALREADY_CANCELLED = "Booking already cancelled"
    BOOKING_CANNOT_CANCEL = "Cannot cancel this booking"
    INVALID_BOOKING_STATUS = "Invalid booking status"
    
    # Product exceptions
    PRODUCT_NOT_FOUND = "Product not found"
    PRODUCT_NAME_EXISTS = "Product name already exists"
    PRODUCT_DELETED = "Product has been deleted"
    
    # Category exceptions
    CATEGORY_NOT_FOUND = "Category not found"
    CATEGORY_NAME_EXISTS = "Category name already exists"
    CATEGORY_HAS_PRODUCTS = "Category has products, cannot delete"
    
    # File exceptions
    FILE_NOT_FOUND = "File not found"
    FILE_URL_EXISTS = "File URL already exists"
    INVALID_FILE_TYPE = "Invalid file type"
    FILE_TOO_LARGE = "File size too large"
    
    # Role/Permission exceptions
    ROLE_NOT_FOUND = "Role not found"
    PERMISSION_NOT_FOUND = "Permission not found"
    ROLE_NAME_EXISTS = "Role name already exists"
    
    # Review exceptions
    REVIEW_NOT_FOUND = "Review not found"
    REVIEW_ALREADY_EXISTS = "User already reviewed this product"
