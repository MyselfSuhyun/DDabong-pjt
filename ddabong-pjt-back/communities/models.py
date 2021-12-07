from django.db import models
from django.conf import settings
from movies.models import Genre

# auto_now_add : 최초 생성 일자
# auto_now : 최종 수정 일자

# 게시판 모델
class Community(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    # upload_to 에 저장된다. blank 는 공백이여도 된다는 뜻이다.
    # 해당 필드를 사용하기 위해서는 Pillow 라이브러리 설치를 필요로 한다.
    image=models.ImageField(blank=True,upload_to=f'communities/images/%Y%m%d%M%S')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name= 'like_communities')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name= 'dislike_communities')
    hits = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 댓글 모델
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    community = models.ForeignKey(Community,on_delete=models.CASCADE,related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content