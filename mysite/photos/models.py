import datetime

from django.db import models


# Create your models here.
class UploadPhoto(models.Model):
    file = models.FileField(upload_to="uploads")