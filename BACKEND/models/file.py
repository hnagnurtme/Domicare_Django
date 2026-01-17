"""File Model"""
from django.db import models
from django.utils import timezone


class File(models.Model):
    """File model - maps to FILES table"""
    id = models.BigAutoField(primary_key=True)
    create_by = models.CharField(max_length=255, default='system')
    update_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    url = models.URLField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'files'
        managed = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Handle audit fields (matches @PrePersist/@PreUpdate)
        if not self.pk:
            if not self.created_at:
                self.created_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)
