from rest_framework.views import APIView
from .models import Game
from .serializer import GamesSerializer
from rest_framework.response import Response
from rest_framework import status
class GamesApi(APIView):
    def get(self, request, format=None):
        serialized = GamesSerializer(Game.objects.all(), many=True)
        return Response(serialized.data, status=200)



    def post(self, r, format=None):
        serialized = GamesSerializer(data=r.data)
        if serialized.is_valid(raise_exception=True):
            serialized.save()
            return Response(serialized.data,status=200)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

