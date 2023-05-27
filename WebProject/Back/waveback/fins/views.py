from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response

class FinsView(APIView):
    def get(self, request):
        surfboards = Fins.objects.all()
        serializer = FinsSerializer(surfboards,many = True)

        return Response(serializer.data)