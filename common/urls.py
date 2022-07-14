from django.urls import path

from common.views import SignupView, SigninView

app_name = 'common'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
]
