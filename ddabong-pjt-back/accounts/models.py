from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings

def profiles_image_path(instance,filename):
    # MEDIA_ROOT/user_<pk>/ 경로로 <filename> 이름으로 업로드
    return f'accounts/profile/user_{instance.pk}/{filename}'


# 유저 정보, 팔로우를 확인하기위한 팔로잉, 게시판글에 사용할 닉네임, 프로필 이미지를 등록할 이미지
class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    followings = models.ManyToManyField('self',symmetrical=False,related_name="followers")
    image=models.ImageField(blank=True,null=True,upload_to=profiles_image_path)

# Mylinks 개인 페이지 사이트를 등록하기 위한 모델.
class Mylinks(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    facebook = models.TextField(blank=True)
    twitter = models.TextField(blank=True)
    youtube = models.TextField(blank=True)
    instagram = models.TextField(blank=True)
    git = models.TextField(blank=True)
