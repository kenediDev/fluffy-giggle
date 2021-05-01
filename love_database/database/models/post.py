import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    public_id = models.CharField(max_length=225,null=False, unique=True, default=str(uuid.uuid4()))
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(null=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.updateAt = timezone.now()
        super().save(*args, **kwargs)
