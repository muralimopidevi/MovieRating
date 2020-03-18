from django.contrib import admin
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin
from .models import Post, Movies, Rating, Opinion


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


@admin.register(Post)
class PostAdmin(ImportExportModelAdmin, ):
    pass


class MoviesResource(resources.ModelResource):
    class Meta:
        model = Movies


@admin.register(Movies)
class MoviesAdmin(ImportExportModelAdmin, ):
    pass


class RatingResource(resources.ModelResource):
    class Meta:
        model = Rating


@admin.register(Rating)
class RatingAdmin(ImportExportModelAdmin, ):
    pass


class OpinionResource(resources.ModelResource):
    class Meta:
        model = Opinion


@admin.register(Opinion)
class RatingAdmin(ImportExportModelAdmin, ):
    pass