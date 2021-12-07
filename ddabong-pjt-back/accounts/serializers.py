from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Mylinks
from movies.models import Movie

# 팔로우를 위한 시리얼라이저, 팔로우 목록에서 영화 목록 출력을 도와 준다.
class FollowSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model =Movie
            fields = ('id','title','poster_path')
    
    like_movies = MovieSerializer(many=True,read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id','username','nickname','like_movies')

# 유저 가입 및 profile 을 띄어주기 위한 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id','username','nickname','password','image','followers')
        read_only_fields = (['followers'])

# 유저의 프로필 페이지에 개인 홈페이지를 등록하기 위한 시리얼라이저
class MylinksSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','username','nickname','image')
    user = UserSerializer(read_only=True)

    class Meta:
        model = Mylinks
        fields = '__all__'
