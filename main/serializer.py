from django.db.models import fields
from rest_framework import serializers
from .models import Game
class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"