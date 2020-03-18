from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, User
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin


class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile

#profile import_export
@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin, ):
    pass


class UserResource(resources.ModelResource):
    class Meta:
        model = User


class UserAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UserResource
    pass

#created admin page names
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.site_header = 'Movie Rating Admin'
admin.site.site_title = 'Movie Rating Admin'
admin.site.index_title = 'Admin Page'