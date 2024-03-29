from rest_framework import serializers
from django.contrib.auth.models import User
from users import models


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=20, write_only=True)


class ConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserConfirmation
        fields = ('code',)
