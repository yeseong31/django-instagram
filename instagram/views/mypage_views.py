from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from common.forms import ProfileImageForm
from common.models import CustomUser


@login_required(login_url='common:signin')
def mypage(request):
    if request.method == 'GET':
        return render(request, 'instagram/mypage.html')


@login_required(login_url='common:signin')
def mypage_profile_upload(request):
    """프로필 이미지 등록"""

    if request.method == 'POST':
        form = ProfileImageForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.get(email=request.user.email)
            user.thumbnail = request.FILES['file']
            user.save()
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)
    else:
        return HttpResponseNotAllowed('Allow POST requests only.')


