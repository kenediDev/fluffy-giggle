from django.urls import path, include

urlpatterns = [
        path("user/", include('love_user.urls'))
        ]
