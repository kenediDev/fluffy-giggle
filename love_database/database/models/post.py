import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Comment(models.Model):
    public_id = models.CharField(max_length=225, null=False, unique=True, default=str(uuid.uuid4()))
    comment = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField()

    class Meta:
        ordering = ["-createAt"]

    def save(self, *args, **kwargs):
        self.updateAt = timezone.now()
        super().save(*args, **kwargs)


class Likes(models.Model):
    public_id = models.CharField(max_length=225, null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField()

    class Meta:
        ordering = ["-createAt"]

    def save(self, *args, **kwargs):
        self.updateAt = timezone.now()
        super().save(*args, **kwargs)


class Post(models.Model):
    public_id = models.CharField(
        max_length=225, null=False, unique=True, default=str(uuid.uuid4())
    )
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(null=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ManyToManyField(Comment, related_name="comment_many_to_many")
    likes = models.ManyToManyField(Likes, related_name="like_many_to_many")

    def save(self, *args, **kwargs):
        self.updateAt = timezone.now()
        super().save(*args, **kwargs)
