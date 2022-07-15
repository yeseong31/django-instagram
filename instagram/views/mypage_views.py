from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='common:signin')
def mypage(request, nickname):
    return render(request, 'instagram/mypage.html')
