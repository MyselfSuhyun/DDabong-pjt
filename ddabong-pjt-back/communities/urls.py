from django.urls import path
from . import views
# namespace : 지정된 URL을 고유하게 사용할 수 있다.
app_name = 'communities'
urlpatterns = [
    # 1. 글 보기 및 작성
    path('', views.board_list_create),
    # 2. 글 상세 보기 및 작성
    path('<int:community_pk>/', views.board_update_delete),
    # 3. 글 수정 삭제 가능 여부
    path('<int:community_pk>/communitystate/',views.communitystate),
    # 4. 댓글 보기 및 작성
    path('<int:community_pk>/comments/',views.comment_create),
    # 5. 댓글 수정 및 삭제
    path('comment/<int:comment_pk>/',views.comment_update_delete),
    # 6. 댓글 수정 삭제 가능 여부
    path('comment/<int:comment_pk>/commentstate/',views.commentstate),
    # 7. 좋아요
    path('<int:community_pk>/likes/',views.likes),
    path('<int:community_pk>/dislikes/',views.dislikes),
    path('<int:community_pk>/likestate/',views.likestate),
    # 8. 장르 목록
    path('genres_list/',views.genres_list),
    # 9. 게시판 랭킹
    path('ranking/',views.rankingboards)
]
