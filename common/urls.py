from django.urls import path

from common.views import SignupView, UserActivateView, SigninView

app_name = 'common'

urlpatterns = [
    # 회원가입
    path('signup/', SignupView.as_view(), name='signup'),
    # 로그인
    path('signin/', SigninView.as_view(), name='signin'),
    # 이메일 유효성 검증
    path('activate/<str:uidb64>/<str:token>/', UserActivateView.as_view()),
]
