from rest_framework import serializers
from movies.models import Genre
from .models import Community,Comment
from django.contrib.auth import get_user_model

# 게시판 목록을 출력하기 위한 시리얼라이저
class CommunitySerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','nickname','username',)
    user= UserSerializer(read_only=True)
    class Meta:
        model = Community
        fields = ('id','title','content','genre','user',"hits","like_users",)
        read_only_fields = (['like_users'])

# 게시판 상세보기 를 위한 시리얼라이저
class CommunityDetailSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','nickname','username')
    user= UserSerializer(read_only=True)
    class Meta:
        model = Community
        fields = '__all__'

# 게시판 댓글을 CRUD하기 위한 시리얼라이저
class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','nickname','username',)
    user= UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields ='__all__'
        read_only_fields = (['community'])

# 장르 목록을 출력하기 위한 시리얼라이저
class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id','name',)