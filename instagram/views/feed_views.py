from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, resolve_url
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from instagram.forms import FeedForm
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
def feed_vote(request, feed_pk):
    """게시글 추천"""

    feed = get_object_or_404(Feed, pk=feed_pk)
    if request.user == feed.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
        return
    feed.voter.add(request.user)
    return redirect(f'{resolve_url("instagram:home")}#feed_{feed_pk}')
