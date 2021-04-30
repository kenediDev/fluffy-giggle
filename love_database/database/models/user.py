from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from .base import Base

class Location(models.Model):
    country = models.CharField(max_length=225, null=True)
    province = models.CharField(max_length=225, null=True)
    city = models.CharField(max_length=225, null=True)
    address = models.CharField(max_length=225, null=True)
    updateAt = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.updateAt = timezone.now()
        super().save(*args, **kwargs)

class Accounts(Base):
    avatar = models.ImageField(upload_to="avatar/")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    phone_numbers = PhoneNumberField(null=True)

    def save(self, *args, **kwargs):
        self.updateAt = timezone.now()
        super().save(*args, **kwargs)
    
