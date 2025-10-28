from rest_framework import serializers
from users.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_likes_count(self, obj):
        return obj.likes.count()