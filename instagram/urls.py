from django.conf.urls.static import static
from django.urls import path

from config.settings import base
from instagram.views.base_views import home
from instagram.views.comment_views import comment_create
from instagram.views.mypage_views import mypage
from instagram.views.feed_views import feed_create, feed_vote

app_name = 'instagram'

urlpatterns = [
    # ----- 피드 -----
    # 홈
    path('', home, name='home'),

    # ----- 게시글 -----
    # 등록
    path('feed/create', feed_create, name='feed_create'),
    # 추천
    path('feed/vote/<int:feed_pk>/', feed_vote, name='feed_vote'),

    # ----- 답글 -----
    # 등록
    path('comment/create/<int:feed_pk>/', comment_create, name='comment_create'),

    # ----- 마이페이지 -----
    # 홈
    path('<str:nickname>/', mypage, name='mypage'),
] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
