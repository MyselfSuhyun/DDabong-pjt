from django.contrib import admin
from .models import Community,Comment

# admin 사이트에서 해당 내용을 쉽게 보기 위해 설정함
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk','content','created_at','updated_at')

admin.site.register(Community,CommunityAdmin)
admin.site.register(Comment,CommentAdmin)