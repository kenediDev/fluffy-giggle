from love_post.views.post import PostModelViewSets, UpdateAPIView , PostGenericsAPIView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", PostModelViewSets, basename="post")

urlpatterns = [
        path("", include((router.urls))),
        path("retrieve/updated/<pk>/", UpdateAPIView.as_view(), name="post-update"),
        path('generics/list/', PostGenericsAPIView.as_view(), name='post-generics-list')
        ]
