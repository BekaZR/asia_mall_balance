from django.shortcuts import render
from rest_framework import viewsets
from mainapp.models import (
    User,
    Point
)
from mainapp.serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
