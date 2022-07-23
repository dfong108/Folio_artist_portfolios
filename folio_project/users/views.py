from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import Group

from .models import *
from .serializers import *

# Create your views here.

def homePage(request):
    return HttpResponse('home page')


# ---------------------- ARTIST LIST ----------------------

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# @api_view(['GET'])
# def artistList(request):
#     artists = Artist.objects.all()
#     serializer = ArtistSerializer(artists)
#     return Response(serializer.data)


# ---------------------- GALLERY LIST ----------------------

class GalleryList(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class GalleryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

# def galleryList(request):
#     return HttpResponse('galleries')