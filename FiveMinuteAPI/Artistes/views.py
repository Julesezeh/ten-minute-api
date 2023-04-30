from django.shortcuts import render
from .serializers import ArtisteSerializer
from .models import Artiste
from rest_framework import generics
# Create your views here.


class ListArtistesView(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


class DetailArtistesView(generics.RetrieveAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
