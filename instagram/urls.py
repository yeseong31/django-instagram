from django.conf.urls.static import static
from django.urls import path

from config.settings import base
from instagram.views.base_views import home
from instagram.views.mypage_views import mypage
from instagram.views.upload_views import feed_create, comment_create

app_name = 'instagram'

urlpatterns = [
    # ----- 피드 -----
    # 홈
    path('', home, name='home'),
    # 게시글 등록
    path('feed/create', feed_create, name='feed_create'),
    # 답글 등록
    path('comment/create/<int:feed_id>/', comment_create, name='comment_create'),

    # ----- 마이페이지 -----
    path('<str:nickname>/', mypage, name='mypage'),
] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
