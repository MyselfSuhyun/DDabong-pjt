from django.urls import path
from . import views

urlpatterns = [
    # JSON 으로 Movie LIst 를 부르는 URL
    path('list/',views.movies_list),
    # JSON 으로 Movie detail 를 부르는 URL
    path('list/<int:movie_pk>/',views.movies_detail),
    # JSON 으로 Review List 를 부르는 URL
    path('<int:movie_pk>/review/',views.review),
    path('<int:movie_pk>/reviewstate',views.reviewstate),
    # JSON 으로 Review Update 와 Delete 도와주는 URL
    path('review/<int:review_pk>/',views.review_update_delete),
    # JSON 으로 해당 영화와 동일한 장르 합집합에서 영화 추천 URL
    path('recommendation/<int:movie_pk>/', views.recommendation),
    # JSON 으로 찜하기 기능 해주는 URL과 상태 확인해주는 URL
    path('<int:movie_pk>/likes/',views.likes),
    path('<int:movie_pk>/liked/',views.liked),
    # JSON 추천 알고리즘 1: 찜하기 기준 추천
    path('recommend/',views.algo1_recommend),
    # JSON 으로 영화 좋아요 순 많은 순으로 정렬
    path('ranking/',views.rankingmovies),
    # JSON 으로 좋아한 장르 수 차트로
    path('rankinggr/',views.rankinggenres),
    # JSON 으로 팔로워 수 랭킹
    path('rankingfr/',views.rankingfollowers),
    path('search/', views.search),
    path('recommendation/keywords/', views.keywords,),  
    path('<int:movie_pk>/keyword/save', views.save_keyword,),
]