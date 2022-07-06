from dataclasses import fields
from rest_framework import serializers
from mainapp.models import (
    User,
    Point
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")
        extra_kwargs = {
            "password": {"write_only":True}
        }


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ("user", "click_count", "last_click_date")