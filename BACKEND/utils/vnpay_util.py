"""VNPay Utility Functions"""
import hashlib
import hmac
from urllib.parse import quote, urlencode
from django.conf import settings


class VNPayUtil:
    """
    VNPay utility functions
    Matches VNPayUtil.java
    """
    
    @staticmethod
    def build_query_string(data: dict) -> str:
        """Build query string from data (sorted by key)"""
        sorted_data = sorted(data.items())
        query_params = []
        for key, value in sorted_data:
            if value:
                query_params.append(f"{key}={quote(str(value))}")
        return '&'.join(query_params)
    
    @staticmethod
    def create_signature(data: str, secret_key: str) -> str:
        """Create HMAC SHA512 signature"""
        signature = hmac.new(
            secret_key.encode('utf-8'),
            data.encode('utf-8'),
            hashlib.sha512
        ).hexdigest()
        return signature
    
    @staticmethod
    def validate_signature(vnpay_params: dict, secret_key: str) -> bool:
        """Validate VNPay signature"""
        secure_hash = vnpay_params.pop('vnp_SecureHash', None)
        if not secure_hash:
            return False
        
        query_string = VNPayUtil.build_query_string(vnpay_params)
        calculated_hash = VNPayUtil.create_signature(query_string, secret_key)
        
        return secure_hash == calculated_hash
    
    @staticmethod
    def get_vnpay_url(params: dict) -> str:
        """Get VNPay payment URL"""
        query_string = VNPayUtil.build_query_string(params)
        secret_key = settings.VNPAY_HASH_SECRET
        
        # Create secure hash
        secure_hash = VNPayUtil.create_signature(query_string, secret_key)
        
        # Build final URL
        vnpay_url = settings.VNPAY_URL
        return f"{vnpay_url}?{query_string}&vnp_SecureHash={secure_hash}"
