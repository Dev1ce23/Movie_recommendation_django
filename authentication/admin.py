from django.contrib import admin
from .models import Movie
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class Moviedata(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Movie, Moviedata)  