from django.db import models
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField

class RegisteredFaces(models.Model):
    created = models.DateTimeField(default=now, editable= False)
    identification_number = models.CharField(blank=False, max_length=15)
    image_path = models.CharField(blank=False, max_length= 300)
    image_encoding = models.BinaryField(blank=False, max_length=900000)