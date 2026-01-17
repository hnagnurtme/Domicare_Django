"""Role Model"""
from django.db import models
from django.utils import timezone


class Role(models.Model):
    """Role model - maps to ROLES table"""
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    create_by = models.CharField(max_length=255, default='system')
    update_by = models.CharField(max_length=255, blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(blank=True, null=True)

    # Relationships
    permissions = models.ManyToManyField(
        'Permission',
        through='PermissionRole',
        related_name='roles'
    )

    class Meta:
        db_table = 'roles'
        managed = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Handle audit fields (matches @PrePersist/@PreUpdate)
        if not self.pk:
            if not self.create_at:
                self.create_at = timezone.now()
        else:
            self.update_at = timezone.now()
        super().save(*args, **kwargs)


class PermissionRole(models.Model):
    """Join table permissions_roles"""
    role = models.ForeignKey(Role, on_delete=models.CASCADE, db_column='role_id')
    permission = models.ForeignKey('Permission', on_delete=models.CASCADE, db_column='permission_id')

    class Meta:
        db_table = 'permissions_roles'
        managed = True
        unique_together = ('role', 'permission')
