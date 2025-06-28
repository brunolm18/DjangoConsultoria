from django.contrib import admin
from .models import Project,Asesoria
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_filter = ['name','date']
    date_hierarchy = "date"
    list_per_page = 10
    search_fields = ['name','image']
    ordering = ['-date',]
    preserve_filters = False
    search_fields = ['name',]


@admin.register(Asesoria)

class AsesoriaAdmin(admin.ModelAdmin):

    list_display = ['user','tema']
    list_per_page = 5

    