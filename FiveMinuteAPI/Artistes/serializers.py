from rest_framework import serializers
from .models import Artiste


class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Artiste
