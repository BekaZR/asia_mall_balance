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