from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # 1. 가입하기
    path('signup/',views.signup),
    # 2. 로그인 유효성 검사를 위한 url
    path('login/',views.login),
    # 3. JWT 토큰을 POST 요청을 통해 얻도록 함 
    path('api-token-auth/',obtain_jwt_token),
    # 4. 프로필 검색하기
    path('search/',views.usersearch),
    # 5. 프로필 페이지
    path('<username>/',views.profile),
    # 6. 프로필 페이지 수정을 위한 url
    path('<username>/validation/',views.validation),
    # 7. 링크 조회 및 추가를 위한 url
    path('<username>/mylinks/',views.mylinks),
    # 8. 링크 수정을 위한 url
    path('<int:link_pk>/linksupdate/',views.mylinks_update),
    # 9. 찜한 영화 목록을 보기 위한 url
    path('<username>/likemovies/',views.likemovies),
    # 10. 팔로잉을 도와주기 위한 url
    path('<username>/follow/',views.follow),
    # 11. 팔로잉을 확인하기 위한 url
    path('<username>/followed/',views.followed),
    # 12. 팔로잉 목록 출력 url
    path('<username>/followings/',views.followings),
    # 13. 팔로워 목록 출력 url
    path('<username>/followers/',views.followers),
    # 14. 내가 쓴 글 목록 출력 url
    path('<username>/myboards/',views.myboards),
    # 15. 운영자 확인, url에 admin 이 포함되면 되지않는다. 신기신기
    path('',views.adminvalid),
    # 16. 프로필 이미지 업로드
    path('<username>/upload/',views.upload),
]