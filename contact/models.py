from django.db import models

# Model for the contact form
class Contact(models.Model):
    subject = models.CharField(max_length=120, blank=False, null=True)
    name = models.CharField(max_length=120, blank=False, null=True)
    email = models.EmailField(max_length=120, blank=False)
    message = models.TextField(blank=False)


    def __str__(self):
        return self.name
