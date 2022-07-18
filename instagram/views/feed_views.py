from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, resolve_url, render
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
        context = {'message': '본인의 게시글은 추천할 수 없습니다.',
                   'url': f'{resolve_url("instagram:home")}#feed_{feed_pk}'}
        return render(request, 'message.html', context, status=HTTP_200_OK)
    if request.user in feed.voter.all():
        feed.voter.remove(request.user)
    else:
        feed.voter.add(request.user)
    return redirect(f'{resolve_url("instagram:home")}#feed_{feed_pk}')
