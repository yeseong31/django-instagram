from django.contrib.auth import views as auth_views
from django.urls import path

from common.views import SignupView, UserActivateView, SigninView, change_password

app_name = 'common'

urlpatterns = [
    # 회원가입
    path('signup/', SignupView.as_view(), name='signup'),
    # 로그인
    path('signin/', SigninView.as_view(), name='signin'),
    # 로그아웃
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # 이메일 유효성 검증
    path('activate/<str:uidb64>/<str:token>/', UserActivateView.as_view()),

    # 비밀번호 변경
    path('change/password/', change_password, name='change_password'),
]
