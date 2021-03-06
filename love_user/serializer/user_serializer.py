from rest_framework import serializers
from django.utils.translation import gettext as _
from database.models import Accounts, Location, Biodata, Interested
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
        bio = Biodata()
        bio.save()
        create.accounts_set.create(location=location, bio=bio)
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
        if self.context["args"] == "accounts":
            instance.first_name = validated_data.get("first_name")
            instance.last_name = validated_data.get("last_name")
            instance.save()
            return self.update_accounts(instance, validated_data)
        if self.context["args"] == "bio":
            return self.update_bio(instance.accounts_set.first(), validated_data)
        return instance

    def update_accounts(self, instance, validated_data):
        instance = instance.accounts_set.first()
        if validated_data.get("avatar"):
            if instance.avatar:
                split = str(instance.accounts.avatar).split("/")
                path = split[len(split) - 1]
                os.system("rm media/avatar/%s" % path)
            instance.avatar = validated_data.get("avatar")

        instance.gender = validated_data.get("gender")
        instance.phone_numbers = validated_data.get("phone_numbers")
        instance.save()
        self.update_location(instance, validated_data)
        return instance

    def update_location(self, instance, validated_data):
        instance.location.country = validated_data.get("country")
        instance.location.province = validated_data.get("province")
        instance.location.city = validated_data.get("city")
        instance.location.address = validated_data.get("address")
        instance.location.save()
        return instance

    def update_bio(self, instance, validated_data):
        instance.bio.bio = validated_data.get("bio")
        if validated_data.get("name"):
            interested = (
                instance.bio.interested.all()
                .filter(name=validated_data.get("name"))
                .first()
            )
            if interested:
                instance.bio.interested_
            instance.bio.interested.add(
                self.update_interested(instance, validated_data)
            )
        instance.bio.save()
        return instance

    def update_interested(self, instance, validated_data):
        create = Interested(name=validated_data.get("name"))
        create.save()
        return create


class InterestedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interested
        exclude = ["id"]


class BioModelSerializer(serializers.ModelSerializer):
    interested = InterestedModelSerializer(read_only=True, many=True)

    class Meta:
        model = Biodata
        exclude = ["id"]


class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ["id"]


class AccountsModelSerializer(serializers.ModelSerializer):
    bio = BioModelSerializer(read_only=True)

    class Meta:
        model = Accounts
        exclude = ["id"]

    location = serializers.SerializerMethodField("get_location_display")
    gender = serializers.SerializerMethodField("get_gender_display")

    def get_gender_display(self, info):
        if info.gender:
            return info.get_gender_display()
        return info.gender

    def get_location_display(self, info):
        serializer = LocationModelSerializer(info.location)
        return serializer.data


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "accounts",]

    accounts = serializers.SerializerMethodField("get_accounts_display")

    def get_accounts_display(self, info):
        serializer = AccountsModelSerializer(info.accounts_set.first())
        return serializer.data
