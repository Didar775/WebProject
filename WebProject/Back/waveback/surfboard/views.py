from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response

class Surfboards(APIView):
    def get(self, request):
        surfboards = Surfboard.objects.all()
        serializer = SurfboardSerializer(surfboards,many = True)

        return Response(serializer.data)