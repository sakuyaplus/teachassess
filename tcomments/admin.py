from django.contrib import admin

# Register your models here.



from .models import TComment

class TCommentAdmin(admin.ModelAdmin):
    list_display=('user_id','user_name','teacher_id','stars','message','comment_date')
    list_display_links=('user_id','user_name',"teacher_id","stars")
    list_per_page=20

admin.site.register(TComment,TCommentAdmin)