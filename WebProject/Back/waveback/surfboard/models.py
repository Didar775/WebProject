from django.db import models


# Create your models here.

class Surfboard(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='surf_boards/', blank=True, null=True)
    rating = models.FloatField(default=0)

    

