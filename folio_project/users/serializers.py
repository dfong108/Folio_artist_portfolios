from pyexpat import model
from rest_framework import serializers, generics
from .models import *

# ------------------ ENTRY FILE SERIALIZER ------------------

# class EntryFileSerializer(serializers.ModelSerializer):




# ------------------ GALLERY ENTRY SERIALIZER ------------------

class GalleryEntrySerializer(serializers.ModelSerializer):

    # files = EntryFileSerializer(many=True)

    class Meta:
        model = GalleryEntry
        fields = ('entry_id', 'title', 'description')


# ------------------ GALLERY SERIALIZER ------------------

class GallerySerializer(serializers.ModelSerializer):

    entries = GalleryEntrySerializer(many=True)

    class Meta:
        model = Gallery
        fields = ('_id', 'title', 'artist', 'description', 'date_created', 'entries')

    # def create(self, validated_data):
    #     # return super().create(validated_data)
    #     entries_data = validated_data.pop('entries')
    #     gallery = Gallery.objects.create(**validated_data)
    #     for entry in entries_data:
    #         GalleryEntry.objects.create(gallery=gallery, **entries_data)
    #     return gallery

# ------------------ ARTIST SERIALIZER ------------------

class ArtistSerializer(serializers.ModelSerializer):

    gallery = GallerySerializer(many=True)

    class Meta:
        model = Artist
        fields = ('_id', 'first_name', 'last_name', 'email', 'artist_type', 'alias', 'about', 'date_created', 'gallery', 'date_created')
        # fields = ('_id', 'first_name' 'last_name', 'email', 'password', 'artist_type', 'alias', 'about', 'deate_created', 'gallery', 'date_created')
    
    def create(self, validated_data):
        # return super().create(validated_data)
        galleries_data = validated_data.pop('gallery')
        artist = Artist.objects.create(**validated_data)
        for gallery in galleries_data:
            Gallery.objects.create(artist=artist, **gallery)
        return artist