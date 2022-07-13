from django.urls import path

from instagram.views.base_views import Main

app_name = 'instagram'

urlpatterns = [
    path('', Main.as_view()),
]
