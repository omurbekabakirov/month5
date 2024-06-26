from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from users.models import UserConfirmation
from users.serializers import RegisterSerializer, ConfirmationSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from users import models
import random


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.create_user(**serializer.validated_data, is_active=False)
    confirm = models.UserConfirmation.objects.create(user=user, code=random.randint(100000, 999999))
    return Response({"code": confirm.code}, status=status.HTTP_200_OK )


@api_view(['POST'])
def confirm(request):
    serializer = ConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = serializer.validated_data.get('code', None)
    confirmation = get_object_or_404(UserConfirmation, code=code)
    user = confirmation.user
    user.is_active = True
    user.save()
    return Response({'status': 'success'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def Login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(serializer.validated_data)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        user.save()
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'status': 'bad request'}, status=400)

