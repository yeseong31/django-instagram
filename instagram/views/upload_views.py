from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from instagram.forms import UploadFeedForm


@login_required(login_url='common:signin')
def upload_feed(request):
    if request.method == 'POST':
        form = UploadFeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.image = request.FILES['file']
            feed.author = request.user
            feed.save()
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)
