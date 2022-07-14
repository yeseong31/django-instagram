from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.generics import get_object_or_404
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from common.forms import UserCreationForm, UserSigninForm
from common.messages import message
from common.models import CustomUser
from common.tokens import account_activation_token


class SignupView(APIView):
    """회원가입"""

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # ----- 이메일 인증 -----
            current_site = get_current_site(request)
            domain = current_site.domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            message_data = message(domain, uidb64, token, 'accounts')

            mail_title = "Instagram: 이메일 인증을 완료해 주세요."
            EmailMessage(mail_title, message_data, to=[form.cleaned_data.get('email')]).send()

            context = {'message': '회원가입 성공! 이메일 인증 링크를 확인해 주세요.', 'url': '/accounts/signin/'}
            return render(request, 'message.html', context, status=HTTP_200_OK)

        # 폼이 유효하지 않은 경우
        context = {'message': '유효하지 않은 폼입니다.', 'url': '/accounts/signin/'}
        return render(request, 'message.html', context, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        return render(request, 'common/signup.html')


class SigninView(APIView):
    """로그인"""

    def post(self, request):
        form = UserSigninForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('/')
            context = {'message': '로그인 실패. 다시 시도 바랍니다.', 'url': '/accounts/signin/'}
            return render(request, 'message.html', context, status=HTTP_400_BAD_REQUEST)

        # 폼이 유효하지 않은 경우
        context = {'message': '로그인 실패', 'url': '/accounts/signin/'}
        return render(request, 'message.html', context, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        form = UserSigninForm()
        return render(request, 'common/signin.html', {'form': form})


class UserActivateView(APIView):
    """이메일 인증 및 사용자 활성화"""

    def get(self, request, uidb64, token):
        try:
            user = get_object_or_404(CustomUser, pk=force_str(urlsafe_base64_decode(uidb64)))
        except(TypeError, ValueError, OverflowError):
            user = None
        # Token 유효성 검증
        if user is not None:
            if account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                context = {'message': '인증 완료! 로그인을 진행해 주세요.', 'url': '/accounts/signin/'}
                return render(request, 'message.html', context, status=HTTP_200_OK)
            else:
                # 인증 만료 시 해당 계정 삭제
                user.delete()

                context = {'message': '인증이 만료된 링크입니다.', 'url': '/accounts/signin/'}
                return render(request, 'message.html', context, status=HTTP_400_BAD_REQUEST)

        context = {'message': '잘못된 접근입니다.', 'url': '/accounts/signin/'}
        return render(request, 'message.html', context, status=HTTP_401_UNAUTHORIZED)
