from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from mainapp.models import (
    User,
    Point
)
from mainapp.serializers import (
    UserSerializer,
    PointSerializer
    )

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PointView(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
