from django.db import models

# Create your models here.

# make a text field that can hold up to 255 characters:
class Line(models.Model):
	text = models.CharField(max_length=255) 