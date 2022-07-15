from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, resolve_url, render
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from instagram.forms import FeedForm, CommentForm
from instagram.models import Feed


@login_required(login_url='common:signin')
def feed_create(request):
    """게시글 등록"""

    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.image = request.FILES['file']
            feed.author = request.user
            feed.save()
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)
    else:
        return HttpResponseNotAllowed('Allow POST requests only.')


@login_required(login_url='common:signin')
def comment_create(request, feed_id):
    """답글 등록"""

    feed = get_object_or_404(Feed, pk=feed_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.feed = feed
            comment.create_date = timezone.now()
            comment.save()
            return redirect(f'{resolve_url("instagram:home")}#comment_{comment.pk}')
        return render(request, 'instagram/feed.html')
    else:
        return HttpResponseNotAllowed('Allow POST requests only.')
