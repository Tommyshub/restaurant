from django.db import models


class BlogPost(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='static/images/')
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
