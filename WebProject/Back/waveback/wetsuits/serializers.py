from rest_framework import serializers
from .models import *
class WetsuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wetsuit
        fields = ['id', 'name', 'description', 'price', 'category', 'image']
        
    