from django.conf.urls.static import static
from django.urls import path

from config.settings import base
from instagram.views.base_views import home
from instagram.views.comment_views import comment_create, comment_vote
from instagram.views.feed_views import feed_create, feed_vote
from instagram.views.mypage_views import mypage, mypage_profile_upload

app_name = 'instagram'

urlpatterns = [
    # ---------- 피드 ----------
    path('', home, name='home'),
    # 등록
    path('feed/create', feed_create, name='feed_create'),
    # 추천
    path('feed/vote/<int:feed_pk>/', feed_vote, name='feed_vote'),

    # ---------- 답글 ----------
    # 등록
    path('comment/create/<int:feed_pk>/', comment_create, name='comment_create'),
    # 추천
    path('comment/vote/<int:comment_pk>/', comment_vote, name='comment_vote'),

    # ---------- 마이 페이지 ----------
    path('mypage/', mypage, name='mypage'),
    # 프로필 이미지 변경
    path('mypage/profile/upload', mypage_profile_upload, name='mypage_profile_upload'),

] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
