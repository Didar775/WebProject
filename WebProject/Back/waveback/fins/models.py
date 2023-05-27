from django.db import models
# Create your models here.

class Fins(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='fins/', blank=True, null=True)