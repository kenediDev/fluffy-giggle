from rest_framework import serializers
from django.contrib.auth.models import User

class BasePost(serializers.Serializer):
    content = serializers.CharField(max_length=225,required=False)
    photo = serializers.ImageField(required=False)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False)

    class Meta:
        abstract = True

class BaseComment(serializers.Serializer):
    comment = serializers.CharField(required=False, max_length=225)

    class Meta:
        abstract = True

class Base(BasePost, BaseComment):
    class Meta:
        abstract = True
