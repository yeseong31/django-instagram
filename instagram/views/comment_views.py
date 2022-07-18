from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, resolve_url, redirect, render
from django.utils import timezone
from rest_framework.status import HTTP_200_OK

from instagram.forms import CommentForm
from instagram.models import Feed, Comment


@login_required(login_url='common:signin')
def comment_create(request, feed_pk):
    """답글 등록"""

    feed = get_object_or_404(Feed, pk=feed_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.feed = feed
            comment.create_date = timezone.now()
            comment.save()
            return redirect(f'{resolve_url("instagram:home")}#feed_{feed_pk}')
        return render(request, 'instagram/feed.html')
    else:
        return HttpResponseNotAllowed('Allow POST requests only.')


@login_required(login_url='common:signin')
def comment_vote(request, comment_pk):
    """답글 추천"""

    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.author:
        context = {'message': '본인의 답글은 추천할 수 없습니다.',
                   'url': f'{resolve_url("instagram:home")}#comment_{comment_pk}'}
        return render(request, 'message.html', context, status=HTTP_200_OK)
    if request.user in comment.voter.all():
        comment.voter.remove(request.user)
    else:
        comment.voter.add(request.user)
    return redirect(f'{resolve_url("instagram:home")}#comment_{comment_pk}')
