from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Review
from .serializers import ReviewSerializer, UserSerializer
from django.contrib.auth.models import User

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie_title']
    ordering_fields = ['rating', 'created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Create your views here.
