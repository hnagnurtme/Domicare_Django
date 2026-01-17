"""User Model"""
from django.db import models
from django.utils import timezone
from .enums import Gender
import bcrypt


class User(models.Model):
    """User model - maps to USERS table"""
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255, db_column="full_name")
    name_unsigned = models.CharField(max_length=255, blank=True, null=True, db_column="name_unsigned")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    address = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    is_email_confirmed = models.BooleanField(default=False)
    email_confirmation_token = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )
    google_id = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )
    avatar = models.URLField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices(),
        blank=True,
        null=True,
    )
    date_of_birth = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=255, default='system')
    update_by = models.CharField(max_length=255, blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(blank=True, null=True)
    user_total_success_bookings = models.BigIntegerField(default=0)
    user_total_failed_bookings = models.BigIntegerField(default=0)
    sale_total_bookings = models.BigIntegerField(default=0)
    sale_success_percent = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(blank=True, null=True)
    
    # Relationships
    roles = models.ManyToManyField(
        'Role',
        through='UserRole',
        related_name='users',
    )
    
    class Meta:
        db_table = 'users'
        managed = True
    
    def __str__(self):
        return self.email

    def check_password(self, raw_password):
        if not self.password:
            return False
        
        try:
            return bcrypt.checkpw(
                raw_password.encode('utf-8'),
                self.password.encode('utf-8')
            )
        except Exception as e:
            print(f"[ERROR] Bcrypt password check failed: {e}")
            return False

    def set_password(self, raw_password):
        hashed = bcrypt.hashpw(
            raw_password.encode('utf-8'),
            bcrypt.gensalt()
        )
        self.password = hashed.decode('utf-8')

    @property
    def is_authenticated(self):
        """Always return True for authenticated users"""
        return True

    @property
    def is_anonymous(self):
        """Always return False for authenticated users"""
        return False
    
    def save(self, *args, **kwargs):
        # Handle name_unsigned
        if self.full_name:
            import unicodedata
            nfkd = unicodedata.normalize('NFKD', self.full_name)
            self.name_unsigned = ''.join([c for c in nfkd if not unicodedata.combining(c)])
        
        # Handle audit fields
        if not self.pk:
            if not self.create_at:
                self.create_at = timezone.now()
            if not self.user_total_success_bookings:
                self.user_total_success_bookings = 0
            if not self.user_total_failed_bookings:
                self.user_total_failed_bookings = 0
            if not self.sale_total_bookings:
                self.sale_total_bookings = 0
            if not self.sale_success_percent:
                self.sale_success_percent = 0.0
        else:
            self.update_at = timezone.now()
        
        super().save(*args, **kwargs)


class UserRole(models.Model):
    """Join table users_roles"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    role = models.ForeignKey('Role', on_delete=models.CASCADE, db_column='role_id')

    class Meta:
        db_table = 'users_roles'
        managed = True
        unique_together = ('user', 'role')