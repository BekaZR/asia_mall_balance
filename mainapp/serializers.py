from dataclasses import fields
from rest_framework import serializers
from mainapp.models import (
    User,
    Point
)
from datetime import date, timedelta

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "balance")
        read_only_fields = ("balance",)
        extra_kwargs = {
            "password": {"write_only":True}
        }


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ("id", "user", "click_count", "last_click_date")
        read_only_fields = ("user",)
    
    
    def update(self, instance, validated_data):
        if date.today() - instance.last_click_date == timedelta(days=1):
            if instance.click_count == 10:
                instance.add_from_user_balance
                instance.default_value_click_count
                return instance
            
            instance.add_from_user_balance
            instance.add_click_count_from_instance
            return instance
        
        elif date.today() - instance.last_click_date == timedelta(days=0):
            raise serializers.ValidationError({"Wrong date":"You can't get a point twice in a day"})
        
        instance.default_value_click_count
        instance.add_from_user_balance
        return instance