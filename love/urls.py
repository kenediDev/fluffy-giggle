from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include('core.urls')),
    path("api-token-auth/", obtain_jwt_token, name="authtoken"),
    path("api-token-refresh/", refresh_jwt_token, name="authtoken-refresh"),
    path("api-token-verify/", verify_jwt_token, name="authtoken-verify")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
