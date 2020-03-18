import django_filters
from .models import Post, Movies
from django_filters import *


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['movie', 'rating', 'opinion']


class MovieFilter(django_filters.FilterSet):
    imbdrating = django_filters.NumberFilter()
    moviereleaseyear = django_filters.NumberFilter()
    class Meta:
        model = Movies
        fields = {
            'movie': ['icontains'],
        }