from django.shortcuts import render
from rest_framework.views import APIView

from common.models import CustomUser


class SignupView(APIView):
    """회원가입"""

    def get(self, request):
        return render(request, 'common/signup.html')


class SigninView(APIView):
    """로그인"""

    def get(self, request):
        return render(request, 'common/signin.html')
