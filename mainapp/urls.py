from rest_framework.routers import SimpleRouter
from django.urls import path, include
from mainapp.views import (
    UserView
)

router = SimpleRouter()
router.register(r'user', UserView)

urlpatterns = [
]

urlpatterns += router.urls