from django.db import models

class Category(models.TextChoices):
    MENS = 'MENS'
    WOMENS = 'WOMENS'
