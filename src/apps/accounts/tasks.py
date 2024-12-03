from django.utils.timezone import now
from datetime import timedelta
from .models import User
from django.conf import settings

def delete_unverified_users():
    expiration_time = now() - timedelta(days=settings.VERIFY_EXPIRATION_DAYS)
    User.objects.filter(is_verified=False, created_at__lt=expiration_time).delete()

