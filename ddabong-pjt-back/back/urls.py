from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 어드민 사이트를 이용하기 위한 URL
    path('admin/', admin.site.urls),
    # 사용자 가입, 로그인 등을 관리하는 urls
    path('accounts/',include('accounts.urls')),
    # 커뮤니티를 지정하는 urls
    path('communities/',include('communities.urls')),
    # 영화 사이트
    path('movies/', include('movies.urls')),
    # All-auth 를 이용하려고 넣었는데..... ㅠㅠ 아쉽당
    path('accounts/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 업로드 된 파일의 URL == settings.MEDIA_URL
# 위 URL 을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
