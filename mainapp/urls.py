from rest_framework.routers import SimpleRouter
from django.urls import path, include
from mainapp.views import (
    UserView,
    PointView
)

router = SimpleRouter()
router.register(r'user', UserView)
router.register(r'point', PointView)

urlpatterns = [
]

urlpatterns += router.urls