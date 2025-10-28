from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User

class Review(models.Model):
    movie_title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_title} - {self.user.username}"
    
    from django.db.models import Count

likes = models.ManyToManyField(User, related_name='liked_reviews', blank=True)
# Create your models here.
