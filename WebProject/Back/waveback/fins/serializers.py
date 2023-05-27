from rest_framework import serializers
from .models import Fins

class FinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fins
        fields = ['id','name', 'description','price', 'image']
    