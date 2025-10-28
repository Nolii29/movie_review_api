from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
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

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        review = self.get_object()
        review.likes.add(request.user)
        return Response({'status': 'review liked'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        review = self.get_object()
        review.likes.remove(request.user)
        return Response({'status': 'review unliked'}, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from django.db.models import Count

class ReviewViewSet(viewsets.ModelViewSet):
    ...

    @action(detail=False, methods=['get'])
    def top_reviews(self, request):
        movie = request.query_params.get('movie_title')
        if not movie:
            return Response({'error': 'movie_title is required'}, status=400)

        reviews = Review.objects.filter(movie_title__icontains=movie).annotate(
            likes_count=Count('likes')
        ).order_by('-likes_count')[:5]

        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)
# Create your views here.
