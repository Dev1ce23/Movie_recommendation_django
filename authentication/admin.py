from django.contrib import admin
from .models import Movie
# from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group

# Register your models here.
# class Moviedata(ImportExportModelAdmin, admin.ModelAdmin):
#     pass
class MovieAdmin(admin.ModelAdmin):
    list_filter=("Year","Rating")
    list_display=("Title","Plot")

admin.site.register(Movie,MovieAdmin)  
admin.site.unregister(Group)