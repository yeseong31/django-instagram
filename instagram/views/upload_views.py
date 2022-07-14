import os
from uuid import uuid4

from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings.base import MEDIA_ROOT
from instagram.models import Feed


class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')

        Feed.objects.create(
            content=content,
            image=image,
            profile_image=profile_image,
            user_id=user_id,
            like_count=0
        )
        return Response(status=200)
