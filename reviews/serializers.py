from rest_framework import serializers
from .models import Review
from django.contrib.auth.models import User

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_likes_count(self, obj):
        return obj.likes.count()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']