from sre_parse import CATEGORIES
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Artist(models.Model):
    CULINARY = 'culinary'
    MUSICIAN = 'musician'
    PERFORMER = 'performer'
    VISUAL = 'visual'
    WRITER = 'writer'
    OTHER = 'other'
    ARTIST_TYPES = [
        (CULINARY, 'culinary'),
        (MUSICIAN, 'musician'),
        (PERFORMER, 'performer'),
        (VISUAL, 'visual'),
        (WRITER, 'writer'),
        (OTHER, 'other')
    ]
    
    name = models.CharField(max_length=200, null=False, blank=False, default='')
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist_type = models.CharField(max_length=20, choices=ARTIST_TYPES, default=VISUAL)
    alias = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=False, blank=False)
    biography = models.TextField(null=False, blank=False)
    # gallery = models.ForeignKey('Gallery', on_delete=models.PROTECT, related_name='artist')
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.name          

    def get_galleries(self):
        galleries = self.galleries.all()
        gallery_list = []
        for gal in galleries:
            # name = gal.name
            # category = gal.category
            # id = gal._id
            gallery = {'name': gal.name, 'category': gal.category, 'id': gal._id}
            gallery_list.append(gallery)

        return gallery_list                         
        # return [gallery.name for gallery in self.galleries.all()]                          


class Gallery(models.Model):
    CULINARY = 'culinary'
    MUSICIAN = 'musician'
    PERFORMER = 'performer'
    VISUAL = 'visual'
    WRITER = 'writer'
    OTHER = 'other'
    CATEGORIES = [
        (CULINARY, 'culinary'),
        (MUSICIAN, 'musician'),
        (PERFORMER, 'performer'),
        (VISUAL, 'visual'),
        (WRITER, 'writer'),
        (OTHER, 'other')
    ]

    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False, default='')
    artist = models.ForeignKey(Artist, null=False, on_delete=models.CASCADE, related_name='galleries')
    category = models.CharField(max_length=20, choices=CATEGORIES, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.name   

    # def get_artist(self) 