from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, resolve_url, redirect, render
from django.utils import timezone

from instagram.forms import CommentForm
from instagram.models import Feed


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
            return redirect(f'{resolve_url("instagram:home")}#comment_{comment.pk}')
        return render(request, 'instagram/feed.html')
    else:
        return HttpResponseNotAllowed('Allow POST requests only.')