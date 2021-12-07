from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Review, Keyword
from django.db.models  import Q,Count
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from .serializers import MovieListSerializer, MovieSerializer, KeywordListSerializer, ReviewSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def movies_list(request):
    # 전체 영화 조회
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies,many=True)
        return Response(serializer.data)
    # 영화 작성
    elif request.method =='POST':
        if not Movie.objects.filter(tmdb_id=request.data['id']):   
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def movies_detail(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method =='DELETE':
        movie.delete()
        data = {
            'delete': f'데이터 {movie_pk}번이 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    elif request.method =='PUT':
        serializer = MovieSerializer(Movie,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def likes(request,movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie,pk=movie_pk)
        isliked = movie.like_users.filter(pk=request.user.pk).exists()
        if isliked:
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        context = {
            'isLiked':not isliked,
            'likeCount':movie.like_users.count()
        }
        return Response(context,status=status.HTTP_200_OK)
    return Response(status=401)

@api_view(['GET'])
def liked(request,movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie,pk=movie_pk)
        isliked = movie.like_users.filter(pk=request.user.pk).exists()
        context = {
            'isLiked': isliked,
            'likeCount':movie.like_users.count()
        }
        return Response(context,status=status.HTTP_200_OK)
    return Response(status=401)

# 글에 리뷰 등록하기
@api_view(['GET','POST'])
def review(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    if request.method =="GET":
        reviews = Review.objects.filter(movie=movie)
        serializer=ReviewSerializer(reviews,many=True)
        return Response(serializer.data)
    if request.method =="POST":
        if Review.objects.filter(movie=movie_pk,user=request.user).exists():
            context = { 'isReviewed':True}
            return Response(context)
        serializer= ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user,movie=movie)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

# 리뷰 수정하기 & 삭제하기
@api_view(['PUT','DELETE'])
def review_update_delete(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method=='PUT':
        serializer = ReviewSerializer(review,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def reviewstate(request,movie_pk):
    if Review.objects.filter(movie=movie_pk,user=request.user).exists():
        review = Review.objects.get(movie=movie_pk,user=request.user)
        serializer= ReviewSerializer(review)
        return Response(serializer.data)
    return Response()

@api_view(['GET','POST'])
def search(request):
    if request.method == 'POST':
        searched = request.data['searched']
        movies = Movie.objects.filter(Q(title__contains=searched)|Q(overview__contains=searched)) ## 제목, 오버뷰에서 검색어 관련 받아오는 걸로 짜놨음
        serializers = MovieListSerializer(movies, many=True)
        return Response(serializers.data)

@api_view(['GET'])
def recommendation(request, movie_pk):
    # 일단 movie id를 받아서 그걸로 장르 아이디를 찾아야 하는듯
    # 이름이 좀 헷갈림. movie에서의 그냥 id 가 movies_movie_genres에서는 movie_id가 되어있음 주의
    # 현재 movie_pk는 movie에서 맨 앞에 딸린 id와 같은 개념
    # 이걸로 movies_movie_genres에 접근 시도해야 함
    # genres = Genre.objects.get(pk=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    genre_list =  movie.genres.all()
    movies = Movie.objects.filter(pk=0)
    ## 영화 받아오기, 어떻게? 해당 영화의 장르가 고른 영화 장르 안에 있다면!
    for genre in genre_list:
        movies = movies|genre.movie_set.all()
    # 중복만 없애줌. 몇개를 띄울지는 아직 모르니까 냅둠
    movies = movies.distinct()
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def algo1_recommend(request):
    movies = request.user.like_movies.all()
    genres = {
        28:0,12:0,16:0,35:0,
        80:0,99:0,18:0,10751:0,
        14:0,36:0,27:0,10402:0,
        9648:0,10749:0,878:0,10770:0,
        53:0,10752:0,37:0,
    }
    for movie in movies:
        genre_list = movie.genres.all()
        for genre in genre_list:
            genres[genre.id] +=1
    genres.items()
    rst = sorted(genres.items(),key=lambda x: x[1],reverse=True)
    for i in range(len(rst)):
        if rst[i][1]:
            break
    else:
        return Response({'isLikeNone':True})
    result_movies = Movie.objects.filter(genres=rst[0][0])
    for i in range(1,3):
        if rst[i][1]:
            result_movies = result_movies|Movie.objects.filter(genres=rst[i][0])
    result_movies=result_movies.distinct()
    serializer = MovieListSerializer(result_movies,many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def keywords(request):
    if request.method == 'GET':
        keywords = get_list_or_404(Keyword)
        serializer = KeywordListSerializer(keywords,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        # 키워드들을 받아온다.
        keywords = request.data['content']
        # 받아온 키워드를 가진 영화를 뽑아보자.(필터나 if)
        keyword_id = Keyword.objects.filter(content=keywords[0]).values('id')[0]['id']
        movie_list = Movie.objects.filter(my_keywords=keyword_id)
        for key in keywords:
            keyword = Keyword.objects.get(content=key)
            data = keyword.movies.all()
            # 키워드 -> 영화목록을 뽑
            movie_list = movie_list|data
        movie_list=movie_list.distinct()
        serializer = MovieListSerializer(movie_list, many=True)
        return Response(serializer.data)

#입력받은 데이터 저장하는 함수
@api_view(['GET','POST'])
def save_keyword(request, movie_pk):
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=movie_pk)
        # 영화에 걸려있는 모든 키워드를 받아와야 함. 그래서 movie_pk가 필요하겠지.... 맞지?ㅠㅠ
        keywords = movie.my_keywords.all()
        serializer = KeywordListSerializer(keywords, many=True)
        return Response(serializer.data)
    # POST로 받으면 저장을 할 건데....
    if request.method == "POST":
        movie = get_list_or_404(Movie, pk=movie_pk)
        # 키워드가 이미 존재한다면 더 들어가진 말거라~
        if Keyword.objects.filter(movies=movie_pk,content=request.data['content']).exists():
            return Response('이미 존재하는 키워드 입니다.')
        serializer = KeywordListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 그냥 저장하면 안되고
            # 이미 데이터베이스 속에 있는 키워드라면 그 키워드의 id와 연결해줘야 할 듯(이거 맞네!!!! 오예!!!!)
            if Keyword.objects.filter(content=request.data['content']).exists():
                keyword_id = Keyword.objects.filter(content=request.data['content']).values('id')[0]['id']
                keyword = Keyword.objects.get(pk=keyword_id)
                print(keyword, keyword_id)
                keyword.movies.add(movie_pk)
                return Response('그렇단다')
            else:
                serializer.save(movies=movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def rankingmovies(request):
    luc = Movie.objects.annotate(Count('like_users')) #like_users count 라는 뜻
    movie_list = luc.order_by('-like_users__count')[:10]
    serializer = MovieListSerializer(movie_list,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def rankinggenres(request):
    genres = {
        "액션":0,"모험":0,"애니메이션":0,"코미디":0,
        "범죄":0,"다큐멘터리":0,"드라마":0,"가족":0,
        "판타지":0,"역사":0,"공포":0,"음악":0,
        "미스터리":0,"로맨스":0,"SF":0,"TV 영화":0,
        "스릴러":0,"전쟁":0,"서부":0,
    }
    luc = Movie.objects.annotate(Count('like_users')) #like_users count 라는 뜻
    for l in luc:
        if(l.like_users__count):
            genre_list = l.genres.all()
            for genre in genre_list:
                genres[genre.name] +=1
    genres.items()
    rst = sorted(genres.items(),key=lambda x: x[1],reverse=True)
    result = [['장르명','찜한수']]
    for i in rst:
        result.append([i[0],i[1]])
    return Response(result)

@api_view(['GET'])
def rankingfollowers(request):
    fs = get_user_model().objects.annotate(Count('followers'))
    print(fs)
    user_list = fs.order_by('-followers__count')[:10]
    serializer = UserSerializer(user_list,many=True)
    return Response(serializer.data)