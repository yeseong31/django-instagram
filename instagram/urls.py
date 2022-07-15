from django.conf.urls.static import static
from django.urls import path

from config.settings import base
from instagram.views.base_views import home
from instagram.views.upload_views import upload_feed

app_name = 'instagram'

urlpatterns = [
    path('', home, name='home'),
    path('upload/feed', upload_feed, name='upload_feed')
] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
