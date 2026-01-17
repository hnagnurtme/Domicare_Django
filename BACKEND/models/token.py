"""Token Model"""
from django.db import models
from django.utils import timezone
from datetime import timedelta


class Token(models.Model):
    """Token model - maps to TOKENS table"""
    id = models.BigAutoField(primary_key=True)
    refresh_token = models.CharField(max_length=255, unique=True)
    expiration = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    # Relationship
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='refresh_tokens',
        db_column='user_id'
    )

    class Meta:
        db_table = 'tokens'
        managed = True
        indexes = [
            models.Index(fields=['refresh_token'], name='idx_token_refresh_token'),
            models.Index(fields=['user'], name='idx_token_user_id'),
        ]

    def __str__(self):
        return f"Token for {self.user.email}"

    def save(self, *args, **kwargs):
        # Handle defaults (matches @PrePersist)
        if not self.created_at:
            self.created_at = timezone.now()
        if not self.expiration:
            self.expiration = timezone.now() + timedelta(days=1)
        super().save(*args, **kwargs)

    def is_expired(self):
        """Matches isExpired() method"""
        return self.expiration < timezone.now()
