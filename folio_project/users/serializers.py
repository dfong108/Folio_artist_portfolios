from dataclasses import field
from pyexpat import model
from rest_framework import serializers, generics
from traitlets import validate
from .models import *

# ------------------ ENTRY FILE SERIALIZER ------------------

class EntryFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntryFile
        fields = ('public_id', 'url', 'date_created')

    def create(self, validated_data):
        file = EntryFile.objects.create(**validated_data)
        return file

# # # ------------------ GALLERY ENTRY SERIALIZER ------------------

class GalleryEntrySerializer(serializers.ModelSerializer):

    files = EntryFileSerializer(many=True)

    class Meta:
        model = GalleryEntry
        fields = ('entry_id', 'name', 'description', 'files')
        
    def create(self, validated_data):
        files_data = validated_data.pop('files')
        id = validated_data.pop('entry_id')
        entry = GalleryEntry.objects.create( **validated_data)
        return entry

# ------------------ GALLERY SERIALIZER ------------------
class GallerySerializer(serializers.ModelSerializer):

    # entries = GalleryEntrySerializer(many=True)

    class Meta:
        model = Gallery
        fields = ('_id', 'title', 'description', 'date_created', 'entries')
        # fields = ('__all__')

    def create(self, validated_data):
        print(validated_data)
        entries_data = validated_data.pop('entries')
        for entry in entries_data: 
            print(entry.entry_id)
            
        gallery = Gallery.objects.create(entries=entries_data, **validated_data)
        # gallery = Gallery.objects.create(**validated_data)
        # gallery.entries.set(entries_data)
        # gallery.entries_set(entries_data)
        # for entry in entries_data:
        #     GalleryEntry.objects.create(gallery=gallery, **entries_data)
        return gallery

    def get_entries(self, obj):
        return {"entries": obj.entries}

# ------------------ ARTIST SERIALIZER ------------------

class ArtistSerializer(serializers.ModelSerializer):

    gallery = GallerySerializer()

    class Meta:
        model = Artist
        fields = ('_id', 'first_name', 'last_name', 'email', 'artist_type', 'alias', 'about', 'date_created', 'gallery', 'date_created')
        # fields = ('_id', 'first_name' 'last_name', 'email', 'password', 'artist_type', 'alias', 'about', 'deate_created', 'gallery', 'date_created')
    
    def create(self, validated_data):
        gallery_data = validated_data.pop('gallery')
        # entry_data = gallery_data.pop('entries')
        artist = Artist.objects.create(**validated_data)
        # artist_id = artist._id
        for gal in gallery_data:
            Gallery.objects.create(artist=artist, **gallery_data)
        return artist