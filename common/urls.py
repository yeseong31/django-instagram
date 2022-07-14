from django.urls import path

from common.views import SignupView

app_name = 'common'

urlpatterns = [
    path('signup/', SignupView.as_view()),
]
