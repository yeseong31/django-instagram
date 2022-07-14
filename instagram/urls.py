from django.conf.urls.static import static
from django.urls import path

from config.settings import base
from instagram.views.base_views import Main
from instagram.views.upload_views import UploadFeed

app_name = 'instagram'

urlpatterns = [
    path('', Main.as_view()),
    path('content/upload', UploadFeed.as_view())
]

urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
