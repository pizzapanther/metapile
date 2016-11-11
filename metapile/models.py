from django.db import models
from django.contrib.postgres.fields import JSONField

class Photo (models.Model):
  path = models.CharField(max_length=255)
  bucket = models.CharField(max_length=255)
  metadata = JSONField(null=True)
  