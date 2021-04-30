from django.urls import path, include
from love_user.views.user import UserModelViewSets, UserAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", UserModelViewSets, basename="user")

urlpatterns = [
    path("", include((router.urls))),
    path("reset/password/", UserAPIView.as_view(), name="user-reset"),
]
