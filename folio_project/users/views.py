from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.urls import is_valid_path

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import Group

# from .models import *
# from .serializers import *
from .models import Artist
from .serializers import ArtistSerializer


# ---------------------- ARTIST LIST ----------------------

class ArtistListCreateAPIView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # permissions = (permissions.AllowAny)
    # def perform_create(self, serializer):
    #     # serializer.save(artist.gallery = self.request.artist.id)
    #     galleryArtist = serializer.validated_data.get('artist.first_name')
    #     print('galleryArtist', galleryArtist)
    #     # return super().perform_create(serializer)



class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer



# Create your views here.

def homePage(request):
    return HttpResponse('home page')

# @api_view(['GET'])
# def artistList(request):
#     artists = Artist.objects.all()
#     serializer = ArtistSerializer(artists, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def createArtist(request):
#     newArtist = Artist.objects.all()
#     serializer = ArtistSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     # return Response(serializer.data)
#     return JsonResponse(serializer.data)

# @api_view(['POST'])
# def updateArtist(request, pk):
#     artist = Artist.objects.get(id, pk)
#     serializer = ArtistSerializer(instance=artist, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def deleteArtist(request, pk):
#     artist = Artist.objects.get(id, pk)
#     artist.delete()
  
#     return Response('item')

