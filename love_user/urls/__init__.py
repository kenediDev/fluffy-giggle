from django.urls import path, include
from love_user.views.user import (
    UserModelViewSets,
    UserAPIView,
    UserGenericAPIView,
    UpdateAPIView,
    UpdateBioAPIView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", UserModelViewSets, basename="user")

urlpatterns = [
    path("", include((router.urls))),
    path("accounts/reset/password/", UserAPIView.as_view(), name="user-reset"),
    path("accounts/list/", UserGenericAPIView.as_view(), name="user-generic-list"),
    path("accounts/updated/", UpdateAPIView.as_view(), name="user-update"),
    path("accounts/bio/updated/", UpdateBioAPIView.as_view(), name="user-bio-update"),
]
