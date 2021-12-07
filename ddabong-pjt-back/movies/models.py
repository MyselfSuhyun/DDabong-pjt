from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    # unique key로 중복 확인하기 위한 모델
    tmdb_id = models.IntegerField(blank=True)
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    overview = models.TextField(blank=True)
    genres = models.ManyToManyField(Genre)
    vote_average = models.FloatField()
    vote_count = models.IntegerField(blank=True)
    popularity =  models.FloatField(blank=True)
    # 상영 시간
    runtime = models.IntegerField(blank=True)
    # keyword =  models.IntegerField(blank=True)
    # 키워드를 빼야 데이터 삽입이 가능했음
    like_users= models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="like_movies")

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    stars = models.FloatField(default=2.5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

# 키워드는 별점이 아니다 나 자신....
class Keyword(models.Model):
    movies = models.ManyToManyField(Movie, blank=True, related_name='my_keywords')
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content