from django.contrib import admin

# Register your models here.
from .models import Academy

class AcademyAdmin(admin.ModelAdmin):
    list_display=['academy_name']
    list_per_page=20

admin.site.register(Academy,AcademyAdmin)