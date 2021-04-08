from django.db import models


class Tips(models.Model):
    tips = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name
