"""Review Model"""
from django.db import models
from django.utils import timezone


class Review(models.Model):
    """Review model - maps to REVIEWS table"""
    id = models.BigAutoField(primary_key=True)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=255, default='system')
    update_by = models.CharField(max_length=255, blank=True, null=True)
    
    # Relationships
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='reviews',
        db_column='user_id'
    )
    
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='reviews',
        db_column='product_id'
    )
    
    class Meta:
        db_table = 'reviews'
        managed = True
    
    def __str__(self):
        return f"Review by {self.user.email} for {self.product.name} - {self.rating}★"
    
    def save(self, *args, **kwargs):
        # Handle audit fields (matches @PrePersist/@PreUpdate)
        if not self.pk:
            if not self.create_at:
                self.create_at = timezone.now()
        else:
            self.update_at = timezone.now()
        super().save(*args, **kwargs)
