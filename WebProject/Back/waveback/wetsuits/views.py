from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import  *
from .models import *
from rest_framework.response import Response
from django.http import JsonResponse

class WetsuitsView(APIView):
    def get(self, request):
        wetsuits = Wetsuit.objects.all()
        print(wetsuits)
        serializer = WetsuitSerializer(data=wetsuits, many = True)
        serializer.is_valid(raise_exception=False)
        serializer.save()
        return Response(status=200, data=serializer.data)
          
    
    

class WetsuitsByCategoryView(APIView):

    def get_object(self, category):
        try:
            return Wetsuit.objects.filter(category = category)
        except Wetsuit.DoesNotExist:
            raise Http404
        
    def get(self, request, category):
        wetsuits = self.get_object(category)
        print(wetsuits)
        serializers = WetsuitSerializer(wetsuits, many = True)
        return Response(serializers.data)

# Create your views here.
