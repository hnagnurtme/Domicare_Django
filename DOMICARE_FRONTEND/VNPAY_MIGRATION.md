# VNPay API Migration to Backend

## Endpoints cần implement trong Spring Boot:

### 1. POST /api/vnpay/create-payment
**Request Body:**
```json
{
  "amount": 100000,
  "orderInfo": "Payment for order #123",
  "orderId": "ORDER123"
}
```

**Response:**
```json
{
  "paymentUrl": "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html?..."
}
```

**Logic:**
- Get TMN_CODE và SECURE_HASH từ application.properties
- Tạo VNPay payment URL với các tham số
- Return URL về frontend

### 2. GET /api/vnpay/vnpay-return
**Query Parameters:**
- vnp_Amount
- vnp_TxnRef (orderId)
- vnp_ResponseCode
- vnp_SecureHash
- ... (các params khác từ VNPay)

**Logic:**
- Verify signature từ VNPay
- Check transaction status
- Update order status trong database
- Redirect về frontend với kết quả

## Dependencies cần thêm vào pom.xml:
```xml
<!-- VNPay hoặc implement manual theo docs -->
```

## Configuration (application.properties):
```properties
vnpay.tmn.code=${VITE_TMN_CODE}
vnpay.secure.hash=${VITE_SECURE_HASH}
vnpay.url=https://sandbox.vnpayment.vn
vnpay.return.url=${VITE_VNP_RETURN_URL}
```

## Frontend changes:
- Xóa folder `/api`
- Cập nhật API calls từ `/api/vnpay/*` sang backend URL
