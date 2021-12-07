from django.shortcuts import get_object_or_404
from .models import Community,Comment
from movies.models import Genre
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import CommentSerializer, GenreListSerializer,CommunitySerializer,CommunityDetailSerializer
from django.db.models  import Count

# 1. 글 보기 및 글 작성
@api_view(['GET', 'POST'])
def board_list_create(request):
    if request.method == 'GET':
        todos = Community.objects.all()
        serializer = CommunitySerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 2.글 상세 보기
@api_view(['GET','PUT', 'DELETE'])
def board_update_delete(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    if request.method == 'GET':
        community.hits +=1
        community.save()
        serializer = CommunityDetailSerializer(community)
        return Response(serializer.data)
    if not request.user.community_set.filter(pk=community_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)
    if request.method == 'PUT':
        serializer = CommunitySerializer(community, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        community.delete()
        return Response({ 'id': community_pk }, status=status.HTTP_204_NO_CONTENT)

# 내가 작성한 글인지 확인하기
@api_view(['GET'])
def communitystate(request,community_pk):
    if request.user.is_authenticated:
        isboard =  request.user.community_set.filter(pk=community_pk).exists()
        context = {
            'isBoard': isboard,
        }
        return Response(context)
    return Response(status=401)

# 글에 댓글 등록하기
@api_view(['GET','POST'])
def comment_create(request,community_pk):
    community = get_object_or_404(Community,pk=community_pk)
    if request.method =="GET":
        comments = Comment.objects.filter(community=community)
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)
    if request.method =="POST":
        serializer= CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user,community=community)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

# 댓글 수정하기 & 삭제하기
@api_view(['PUT','DELETE'])
def comment_update_delete(request,comment_pk):
    # # community = get_object_or_404(Community,pk=community_pk)
    comment = Comment.objects.get(pk=comment_pk)
    # print(request.data)
    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

    if request.method=='PUT':
        serializer = CommentSerializer(comment,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)

# 내가 작성한 글인지 확인하기
@api_view(['GET'])
def commentstate(request,comment_pk):
    if request.user.is_authenticated:
        iscomment =  request.user.comment_set.filter(pk=comment_pk).exists()
        context = {
            'isComment': iscomment,
        }
        return Response(context)
    return Response(status=401)

@api_view(['GET'])
def likes(request,community_pk):
    if request.user.is_authenticated:
        community = get_object_or_404(Community, pk=community_pk) 
        isliked = community.like_users.filter(pk=request.user.pk).exists()
        if isliked:
            community.like_users.remove(request.user)
        else:
            community.like_users.add(request.user)
            community.dislike_users.remove(request.user)
        context = {
            'isLiked': not isliked,
        }
        return Response(context)
    return Response(status=401)  

@api_view(['GET'])
def dislikes(request, community_pk):
    if request.user.is_authenticated:
        community = get_object_or_404(Community, pk=community_pk) 
        disliked = community.dislike_users.filter(pk=request.user.pk).exists()
        if disliked:
            community.dislike_users.remove(request.user)
        else:
            community.dislike_users.add(request.user)
            community.like_users.remove(request.user)
        context = {
            'disLiked': not disliked,
        }
        return Response(context)
    return Response(status=401)

@api_view(['GET'])
def likestate(request,community_pk):
    if request.user.is_authenticated:
        community = get_object_or_404(Community, pk=community_pk)
        isliked = community.like_users.filter(pk=request.user.pk).exists() 
        disliked = community.dislike_users.filter(pk=request.user.pk).exists()
        context = {
            'isLiked': isliked,
            'disLiked': disliked,
            'likeCount': community.like_users.filter(pk=request.user.pk).count(),
            'disLikeCount': community.dislike_users.filter(pk=request.user.pk).count()
        }
        return Response(context)
    return Response(status=401)

@api_view(['GET'])
@permission_classes([AllowAny])
def genres_list(request):
    # 전체 장르 조회
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreListSerializer(genres,many=True)
        return Response(serializer.data)
 
@api_view(['GET'])
def rankingboards(request):
    luc = Community.objects.annotate(Count('like_users')) #like_users count 라는 뜻
    board_list = luc.order_by('-like_users__count','-hits')[:10]
    serializer = CommunitySerializer(board_list,many=True)
    return Response(serializer.data)