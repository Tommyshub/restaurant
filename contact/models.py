from django.db import models


# Model for the contact form
class Contact(models.Model):
    subject = models.CharField(max_length=120, null=False, blank=False)
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120 , null=True, blank=True)
    email = models.EmailField(max_length=120, null=False, blank=False)
    message = models.CharField(max_length=780, null=False, blank=False)


    def __str__(self):
        return self.name
