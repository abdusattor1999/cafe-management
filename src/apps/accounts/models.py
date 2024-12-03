from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from .manager import UserManager

class User(AbstractUser):
    ROLE_CHOICES = (
        ('USER', 'User'),
        ('ADMIN', 'Admin'),
    )
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER')
    verification_token = models.UUIDField(default=uuid.uuid4, unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    birthdate = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def get_full_name(self):
        full_name = self.first_name
        if self.last_name:
            full_name += f" {self.last_name}"
        if not full_name:
            return self.get_username()
        return full_name
    

    def verify(self):
        self.is_active = True
        self.verification_token = None
        self.save()

    def __str__(self):
        return self.get_full_name
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

@receiver(post_save, sender=User)
def send_activation_link_for_new_users(sender, instance, created, **kwargs):
    if created:
        pass
        
