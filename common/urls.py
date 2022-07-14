from django.urls import path

from common.views import signup, signin

app_name = 'common'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
]
