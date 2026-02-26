from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class UserOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now=True)

    def is_valid(self):
        # OTP is valid for 5 minutes
        return timezone.now() < self.created_at + datetime.timedelta(minutes=5)

