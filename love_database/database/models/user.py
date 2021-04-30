from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from .base import Base

class AccountsEnum:
    male = 0
    female = 1
    CHOICE = ((male,_("Male")),(female,_("Female")))

class Interested(models.Model):
    name = models.CharField(max_length=225,null=False)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.updateAt = timezone.now()
        super().save(*args, **kwargs)

class Biodata(models.Model):
    bio = models.TextField(null=True)
    interested = models.ManyToManyField(Interested, related_name="interested_many_to_many")
    createAt = models.DateTimeField(auto_now_add=True, null=True)
    updateAt = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.updateAt = timezone.now()
        super().save(*args, **kwargs)

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
    gender = models.IntegerField(choices=AccountsEnum.CHOICE,default=AccountsEnum.male, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    bio = models.ForeignKey(Biodata, on_delete=models.CASCADE, null=True)
    phone_numbers = PhoneNumberField(null=True)

    def save(self, *args, **kwargs):
        self.updateAt = timezone.now()
        super().save(*args, **kwargs)
    
