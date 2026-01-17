"""Permission Model"""
from django.db import models
from django.utils import timezone


class Permission(models.Model):
    """Permission model - maps to PERMISSIONS table"""
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    api_path = models.CharField(max_length=255)
    method = models.CharField(max_length=20)
    module = models.CharField(max_length=100)
    create_by = models.CharField(max_length=255, default='system')
    update_by = models.CharField(max_length=255, blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'permissions'
        managed = True

    def __str__(self):
        return f"{self.module}.{self.name}"

    def save(self, *args, **kwargs):
        # Handle audit fields (matches @PrePersist/@PreUpdate)
        if not self.pk:
            if not self.create_at:
                self.create_at = timezone.now()
        else:
            self.update_at = timezone.now()
        super().save(*args, **kwargs)
