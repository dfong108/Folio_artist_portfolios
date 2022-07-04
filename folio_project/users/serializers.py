from pyexpat import model
from rest_framework import serializers, generics
from .models import *

class ArtistSerializer(serializers.ModelSerializer):

    # galleries = serializers.SerializerMethodField(read_only=True)
    def get_galleries(self, obj):
        return obj.get_galleries()

    class Meta:
        model = Artist
        # fields = ('artist_type', 'name', 'alias', 'galleries')
        fields = '__all__'
    

class GallerySerializer(serializers.ModelSerializer):
    # galleries = serializers.HyperlinkedRelatedField(
    # view_name='GalleryList',
    # many=True,
        # read_only=True
    # )

    class Meta:
        model = Gallery
        # fields = ('name', 'description')
        fields = '__all__'