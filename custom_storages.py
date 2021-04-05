from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# Get the static location from settings.py
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

""" 
Added location for media storage even 
though it will not be used for now.
"""
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION