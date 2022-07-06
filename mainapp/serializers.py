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
        fields = ("username", "password", "balance")
        read_only_fields = ("balance",)
        extra_kwargs = {
            "password": {"write_only":True}
        }
        


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ("user", "click_count", "last_click_date")
        read_only_fields = ("user",)
    
    def update(self, instance, validated_data):
        
        if date.today() - instance.last_click_date == timedelta(days=1):
            if instance.click_count == 10:
                instance.click_count = 1
                instance.user.balance += instance.click_count
                instance.user.save()
                instance.save()
                return instance
            
            instance.user.balance += instance.click_count
            instance.click_count += 1
            instance.user.save()
            instance.save()
            return instance
        
        elif date.today() - instance.last_click_date == timedelta(days=0):
            return instance
        
        instance.click_count = 1
        instance.user.balance += instance.click_count
        instance.user.save()
        instance.save()
        return instance