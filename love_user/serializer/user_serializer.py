from rest_framework import serializers
from django.utils.translation import gettext as _
from database.models import Accounts, Location
from django.contrib.auth.models import User
from love_user.serializer.base import Base
from django.db.models import Q
from django.core.mail import EmailMessage
import os
import dotenv
import re

dotenv.load_dotenv()

r_email = r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"


class UserSerializer(Base):
    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)

    def get_fields(self, *args, **kwargs):
        fields = super(UserSerializer, self).get_fields(*args, **kwargs)
        return fields

    def create(self, validated_data):
        if self.context["args"] == "create":
            return self.create_user(validated_data)
        elif self.context["args"] == "reset":
            return self.reset_user(validated_data)
        return validated_data

    def create_user(self, validated_data):
        if User.objects.filter(
            Q(username=validated_data.get("username"))
            | Q(email=validated_data.get("email"))
        ).first():
            raise serializers.ValidationError(
                {
                    "message": _(
                        "Username or email already exists, please choose another one"
                    )
                }
            )
        if validated_data.get("password") != validated_data.get("confirm_password"):
            raise serializers.ValidationError(
                {"message": _("Password don't match, please check again")}
            )
        create = User(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            password=validated_data.get("password"),
        )
        create.set_password(validated_data.get("confirm_password"))
        create.save()
        location = Location()
        location.save()
        create.accounts_set.create(location=location)
        return create

    def reset_user(self, validated_data):
        user = User.objects.filter(
            Q(username=validated_data.get("token"))
            | Q(email=validated_data.get("token"))
        ).first()
        if not user:
            raise serializers.ValidationError({"message": _("Accounts not found")})
        mail = EmailMessage(
            "Subject", "Hello Wolrds", os.environ.get("smtp_user"), [user.email]
        )
        mail.send()
        return mail

    def update(self, instance, validated_data):
        pass


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
