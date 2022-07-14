from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from common.models import CustomUser


def signup(request):
    pass


def signin(request):
    return render(request, 'common/signin.html')
