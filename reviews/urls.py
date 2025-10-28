from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, UserViewSet, register_user

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'), 
]
