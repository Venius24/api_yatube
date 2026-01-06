from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import PostViewSet, GroupViewSet, CommentViewSet
from .serializers import PostSerializer, GroupSerializer, CommentSerializer


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]