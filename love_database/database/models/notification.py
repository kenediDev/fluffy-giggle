import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .post import Comment, Likes

class Group(models.Model):
    public_id = models.CharField(max_length=225, null=False, unique=True, default=str(uuid.uuid4()))
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    likes = models.ForeignKey(Likes, on_delete=models.CASCADE, null=True)

class Notification(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    notif = models.IntegerField(default=0)
    notifications = models.ManyToManyField(Group)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.updateAt = timezone.now()
        super().save(*args, **kwargs)

