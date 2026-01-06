from django.conf import settings
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
#    path('auth/', include('djoser.urls')),  # базовые (registration, activation и т.д.)
#    path('auth/', include('djoser.urls.jwt')),  # JWT-specific: /auth/jwt/create/ (login), /jwt/refresh/, /jwt/verify/
#    path('api/v1/api-token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#    path('api/v1/api-token-auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
