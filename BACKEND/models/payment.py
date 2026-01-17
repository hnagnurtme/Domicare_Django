"""Payment Transaction Model"""
from django.db import models
from django.utils import timezone
from .enums import PaymentStatus


class PaymentTransaction(models.Model):
    """PaymentTransaction model - maps to PAYMENT_TRANSACTIONS table"""
    id = models.BigAutoField(primary_key=True)
    order_id = models.CharField(max_length=255, unique=True)
    amount = models.BigIntegerField()
    order_info = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices(),
        default=PaymentStatus.PENDING.value
    )
    transaction_no = models.CharField(max_length=255, blank=True, null=True)
    bank_code = models.CharField(max_length=50, blank=True, null=True)
    pay_date = models.CharField(max_length=14, blank=True, null=True)
    response_code = models.CharField(max_length=10, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    
    # Relationship
    booking = models.ForeignKey(
        'Booking',
        on_delete=models.SET_NULL,
        related_name='payments',
        db_column='booking_id',
        null=True,
        blank=True
    )
    
    created_by = models.CharField(max_length=255, default='system')
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'payment_transactions'
        managed = True
    
    def __str__(self):
        return f"Payment {self.order_id} - {self.status}"
    
    def save(self, *args, **kwargs):
        # Handle audit fields (matches @PrePersist/@PreUpdate)
        if not self.pk:
            if not self.created_at:
                self.created_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)
