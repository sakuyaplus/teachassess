from django.contrib import admin

# Register your models here.
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display=('id','name','dept','organs','sex','rank')
    list_display_links=('id','name')
    list_per_page=20

admin.site.register(Teacher,TeacherAdmin)