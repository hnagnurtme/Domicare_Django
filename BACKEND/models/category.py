"""Category Model"""
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """Category model - maps to CATEGORIES table"""
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    name_unsigned = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    create_by = models.CharField(max_length=255, default='system')
    update_by = models.CharField(max_length=255, blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'categories'
        managed = True
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Handle name_unsigned (matches @PrePersist/@PreUpdate)
        if self.name:
            import unicodedata
            nfkd = unicodedata.normalize('NFKD', self.name)
            self.name_unsigned = ''.join([c for c in nfkd if not unicodedata.combining(c)])

        # Handle audit fields
        if not self.pk:
            if not self.create_at:
                self.create_at = timezone.now()
        else:
            self.update_at = timezone.now()

        super().save(*args, **kwargs)
