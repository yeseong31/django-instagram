from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from instagram.models import Feed


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()
        return render(request, 'instagram/feed.html', {'feed_list': feed_list})
