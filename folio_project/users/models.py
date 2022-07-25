from sre_parse import CATEGORIES
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import uuid

from django.forms import model_to_dict

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
    
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, null=True, blank=False)
    last_name = models.CharField(max_length=30, null=True, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    artist_type = models.CharField(max_length=20, choices=ARTIST_TYPES, default=VISUAL)
    alias = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.first_name          


class Gallery(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=False, blank=False, default='No Title')
    artist = models.OneToOneField(Artist, null=False, blank=False, on_delete=models.CASCADE, related_name='gallery')
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    # entries = ArrayField(base_field=model_to_dict(GalleryEntry))

    def __str__(self):
        return str(self.title)

    # def get_artist(self) 


class GalleryEntry(models.Model):
    entry_id = models.CharField(primary_key=True, default='', editable=False, max_length=100)
    name = models.CharField(max_length=200, null=False, blank=False, default='')
    gallery = models.ForeignKey(Gallery, null=False, on_delete=models.CASCADE, related_name='entries')
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.name

class EntryFile(models.Model):
    public_id = models.CharField(primary_key=True, editable=False, max_length=100)
    url = models.CharField(max_length=200, null=False, blank=False, default='')
    gallery_entry = models.ForeignKey(GalleryEntry, null=False, blank=False, on_delete=models.CASCADE, related_name='files')
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.url   