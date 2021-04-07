from django.db import models


class Tips(models.Model):
    tips = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name

