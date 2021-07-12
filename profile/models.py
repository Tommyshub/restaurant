from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from .validators import (validate_phone_number, validate_postal_code,
                         validate_county,
                         validate_city, validate_alpha_numeric)


class UserProfile(models.Model):
    """
    A user profile where the users can handle their
    order information and change delivery
    information if needed.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(validators=[validate_phone_number],
                                            max_length=20, null=True,
                                            blank=False)
    default_street_address1 = models.CharField(
        validators=[validate_alpha_numeric], max_length=80,
        null=True, blank=False)
    default_street_address2 = models.CharField(
        validators=[validate_alpha_numeric], max_length=80,
        null=True, blank=True)
    default_town_or_city = models.CharField(validators=[validate_city],
                                            max_length=40, null=True,
                                            blank=False)
    default_postcode = models.CharField(validators=[validate_postal_code],
                                        max_length=20, null=True,
                                        blank=False)
    default_county = models.CharField(
        validators=[validate_county], max_length=80, null=True, blank=False)
    default_country = CountryField(
        blank_label='Country', null=True, blank=False)


def __str__(self):
    return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the profile for the user
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Save the profile if the user already exists
    instance.userprofile.save()
