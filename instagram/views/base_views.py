from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from instagram.models import Feed


@login_required(login_url='common:signin')
def home(request):
    feed_list = Feed.objects.all().order_by('-id')
    return render(request, 'instagram/feed.html', {'feed_list': feed_list})
