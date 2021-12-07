from rest_framework import serializers
from .models import Movie, Review, Keyword
from django.contrib.auth import get_user_model

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id','title','poster_path','genres','like_users')

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','nickname','username',)
    user= UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields ='__all__'
        read_only_fields = (['movie',])

class KeywordListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = ('movies', 'content',)
        read_only_fields = (['movies',])