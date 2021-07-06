from django.db import models
from profile.models import UserProfile


class BlogPost(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='cars')
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
