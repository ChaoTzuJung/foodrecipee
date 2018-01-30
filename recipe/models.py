# Create your models here.
from django.db import models
from django.utils import timezone


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image_path = models.CharField(max_length=100)
    description = models.TextField()
    create_at = models.TextField(default=timezone.now)
  