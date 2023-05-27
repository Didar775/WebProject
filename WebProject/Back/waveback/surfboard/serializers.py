from rest_framework import serializers
from .models import Surfboard

class SurfboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surfboard
        fields = ['id','name', 'description','price', 'rating', 'image']
    