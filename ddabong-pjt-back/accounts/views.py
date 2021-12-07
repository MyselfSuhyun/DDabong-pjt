from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404,redirect
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import  UserSerializer, MylinksSerializer,FollowSerializer
from rest_framework.permissions import AllowAny
from .models import Mylinks, User
from rest_framework import status
from movies.serializers import MovieListSerializer
from communities.serializers import CommunitySerializer
from django.db.models  import Q
from django.conf import settings

# 1.가입하기: vue 에서 회원가입 할 때
@api_view(['POST'])
# 데코레이터 순서를 신경써야한다.
@permission_classes([AllowAny])
def signup(request):
    # 1-1. Client에서 온 데이터를 받자
    username = request.data.get('username')
    nickname = request.data.get('nickname')
    print(nickname)
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if (8<=len(username)<=12):
        for i in username:
            if '0'<=i<='9' or 'A'<=i<='Z' or 'a'<=i<='z':
                continue
            else:
                return Response('아이디는 대문자,소문자,숫자로만 이루어져야합니다.',status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response('아이디는 8~12자 대문자,소문자, 숫자여야합니다.',status=status.HTTP_400_BAD_REQUEST)

    if (len(nickname)<1 or len(nickname)>6):
        return Response('닉네임은 1글자이상 5글자이야여야합니다.',status=status.HTTP_400_BAD_REQUEST)
    
    if (8<=len(password)<=12):
        for i in password:
            if '0'<=i<='9' or 'A'<=i<='Z' or 'a'<=i<='z':
                continue
            else:
                return Response('비밀번호는 대문자,소문자,숫자로만 이루어져야합니다.',status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response('비밀번호는 8~12자 대문자,소문자, 숫자여야합니다.',status=status.HTTP_400_BAD_REQUEST)
    
    # 1-2 입력한 아이디가 이미 존재하는지 확인하자.
    if User.objects.filter(username=username):
        return Response('존재하는 아이디입니다.',status=status.HTTP_400_BAD_REQUEST)
    # 1-3. password 일치여부 확인, DRF 에서는 별도 구현해야한다. vue 에서 구현했으므로 중복 x
    if password != password_confirmation:
        return Response('비밀번호가 일치하지 않습니다.',status=status.HTTP_400_BAD_REQUEST)
    
    # 2. UserSerializer 를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)

    # 3. validation (password도 같이 직렬화 진행)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 4. 비밀번호 해싱
        user.set_password(request.data.get('password'))
        user.save()
        # password 는 직렬화 과정에는 표현하지만, 표현 할 때는 나타나지않음(serializer의 write_only=True) 때문
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 2.로그인 유효성 검사: 로그인이 유효한지 검색하기 위한 view, 이를 통과하면 token 을 얻는 url 로 연결할 것
@api_view(['POST'])
# 아직 토큰을 얻지 못했으므로 AllowAny 로 설정해준다.
@permission_classes([AllowAny])
def login(request):
    # 1. Client 에서 온 데이터를 받기
    username = request.data.get('username')
    password = request.data.get('password')
    # 1-1. 데이터 입력이 이루어지지 않았다면, 빈칸이라고 alert 를 보내자.
    if not username or not password:
        return Response('빈칸입니다.',status=status.HTTP_400_BAD_REQUEST)
    # 1-2. 데이터베이스에 없는 아이디를 입력했다면,
    if not User.objects.filter(username=username):
        return Response('존재하지 않은 아이디입니다.',status=status.HTTP_400_BAD_REQUEST)
    # 1-3. 아이디를 검색했으니, 그 아이디를 가져와서, password check를 해주자.
    user = User.objects.get(username=username)
    if not user.check_password(password):
        return Response('비밀번호가 일치하지 않습니다.',status=status.HTTP_400_BAD_REQUEST)
    # 2. 유효성 검사를 통과했으므로, True를 반환해주어 토큰을 얻자.
    return Response({'Success':True},status=status.HTTP_200_OK)

# 4. 유저검색
@api_view(['POST'])
def usersearch(request):
    searched = request.data['usersearch']
    users = User.objects.filter(Q(username__contains=searched)|Q(nickname__contains=searched)) ## 제목, 오버뷰에서 검색어 관련 받아오는 걸로 짜놨음
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data)

# 5. 프로필 페이지를 출력하는 view
@api_view(['GET'])
def profile(request,username):
    # 1. 유저목록을 받아온다.
    user = get_object_or_404(get_user_model(),username=username)
    if request.method == 'GET':
        # 2. 시리얼 라이저에 등록하여 응답한다.
        serializers = UserSerializer(user)
        return Response(serializers.data)
    # 3. 그러지 못했을 경우 401 을 응답으로 보낸다.
    return Response(status=status.HTTP_401_UNAUTHORIZED)

# 6. 사용자와 프로필 사람과 동일인지 유효성 확인하는 함수. 이를 통해, 프로필 페이지 수정이 가능하다.
@api_view(['GET'])
def validation(request,username):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(),username=username)
        isValid = request.user==user
        context={
            'isValid':isValid,
        }
        return Response(context)

# 7. mylinks 조회 및 생성
@api_view(['GET','POST'])
def mylinks(request,username):
    # 1. 유저 정보를 조회한다.`
    user = get_object_or_404(get_user_model(),username=username)
    # 2.등록한 개인 홈페이지 링크 정보를 조회한다. 
    if request.method == 'GET':
        mylinks = Mylinks.objects.filter(user=user)
        serializer = MylinksSerializer(mylinks,many=True)
        return Response(serializer.data)
    # 3. 개인 홈페이지 링크를 등록한다.
    elif request.method == 'POST':
        serializer = MylinksSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)


# 8. mylinks 수정 
@api_view(['PUT'])
def mylinks_update(request,link_pk):
    # 1. link_pk 로 링크 데이터를 가져온다.
    mylink= Mylinks.objects.get(pk=link_pk)
    if request.method=="PUT":
        # 2. 정보를 수정한다.
        serializer = MylinksSerializer(mylink,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 9. 찜한 영화 목록을 보자!
@api_view(['GET'])
def likemovies(request,username):
    user = User.objects.get(username=username)
    if request.method=="GET":
        movies = user.like_movies.all()
        serializer = MovieListSerializer(movies,many=True)
        return Response(serializer.data)
    return Response(status=401)

# 10. 팔로우 하기위한 함수
@api_view(['GET'])
def follow(request,username):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(),username=username)
        # 팔로우할 사람과 현재 유저가 달라야지만, 팔로우가 가능하도록 조건문을 건다.
        if person != request.user:
            isFollowed = person.followers.filter(pk=request.user.pk).exists()
            if isFollowed:
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
            # 팔로우 수를 확인하기 위해 count 함수도 사용한다.
            context = {
                'isFollowed': isFollowed,
                'followings': person.followings.count(),
                'followers':person.followers.count()
            }
            return Response(context)
    return Response(status=401)

# 11. 팔로우 상태를 확인하기 위한 함수. 이를 통해, 새로고침하더라도 팔로우 상태를 알 수 있다.
@api_view(['GET'])
def followed(request,username):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(),username=username)
        isFollowed = person.followers.filter(pk=request.user.pk).exists()
        # 새로고침을 하더라도, 필요한 정보를 출력하기 위해 context 에 관련 자료를 담는다.
        context = {
            'isFollowed': isFollowed,
            'followings': person.followings.count(),
            'followers':person.followers.count()
        }
        return Response(context)
    return Response(status=401)

# 12. 팔로잉 목록을 통해, 팔로우 수 와 해당 유저들의 영화 목록을 확인할 수 있다.
@api_view(['GET'])
def followings(request,username):
    person = get_object_or_404(get_user_model(),username=username)
    print(person)
    Followings = person.followings.all()
    serializer = FollowSerializer(Followings,many=True)
    return Response(serializer.data)

# 13. 팔로워 목록을 통해, 팔로워 수와 해당 유저들의 영화 목록을 확인할 수 있다.
@api_view(['GET'])
def followers(request,username):
    person = get_object_or_404(get_user_model(),username=username)
    Followers = person.followers.all()
    serializer = FollowSerializer(Followers,many=True)
    return Response(serializer.data)

# 14. 내가 쓴 글의 목록을 확인하기 위한 views.
@api_view(['GET'])
def myboards(request,username):
    person = get_object_or_404(get_user_model(),username=username)
    boards = person.community_set.all()
    serializer = CommunitySerializer(boards,many=True)
    return Response(serializer.data)

# 15. 어드민인지 확인하는 views. 이를 통해, 관리자 사이트에 접근할 수 있다.
@api_view(['GET'])
def adminvalid(request):
    context = {
        'isAdmined':request.user.is_superuser,
        'currentUser':request.user.username
    }
    return Response(context)

# 16. 프로필 페이지 업로드를 위한 함수.
@api_view(['POST'])
def upload(request,username):
    user = get_object_or_404(get_user_model(),username=username)
    # # 1-1. Client에서 온 데이터를 받자
    # password = request.data.get('newpassword')
    # password_confirmation = request.data.get('newpasswordConfirm')
    # # 1-2. password 일치여부 확인, DRF 에서는 별도 구현해야한다.
    # if password and password_confirmation and password != password_confirmation:
    #     print('확인')
    #     return Response({'error':'비밀번호가 일치하지 않습니다.'},status=status.HTTP_400_BAD_REQUEST)
    # 1-2. password 일치여부 확인, DRF 에서는 별도 구현해야한다.
    if not user.check_password(request.data.get('password')):
        return Response({'error':'비밀번호가 일치하지 않습니다.'},status=status.HTTP_400_BAD_REQUEST)
    if request.method =="POST":
        serializer= UserSerializer(user,data=request.data)
        if serializer.is_valid(raise_exception=True):
            changeuser = serializer.save()
            # if password and password!="":
            #     changeuser.set_password(password)
            # else:
            #     changeuser.set_password(request.data.get('password'))
            changeuser.set_password(request.data.get('password'))
            changeuser.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
