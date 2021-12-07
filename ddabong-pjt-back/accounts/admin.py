from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# 1. 유저 정보를 어드민 사이트에서 조정 가능하다.
admin.site.register(User,UserAdmin)