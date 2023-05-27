from django.db import models
from .choices import *
# Create your models here.




class Wetsuit(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='wet_suits/', blank=True, null=True)
    category = models.CharField(max_length=10, choices=Category.choices, default=Category.MENS)
  
