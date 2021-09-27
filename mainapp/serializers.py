"""Required imports for serializers"""
from copy import Error

from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.validators import UniqueTogetherValidator
import random
from django.utils import timezone


"""SESSION SERIALIZER"""
class SessionYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionYear
        fields = '__all__'


"""SETTINGS SERIALIZER """
class SettingsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Settings
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['running_year'] = SessionYearSerializer(instance.running_year).data
        return response


"""PROFILE IMAGE SERIALIZER"""
class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = '__all__'


""""CUSTOM USER SERIALIZER"""
class CustomUserSerializer(serializers.ModelSerializer):

    """Overding the password hashing problem in Custom User"""
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
    class Meta:
        model = get_user_model()
        fields = ['id','user_type','first_name', 'last_name', 'middleName','profile_pic', 'email','username', 'password', ]
        extra_kwargs = {
            'username' : {
                'validators': [UnicodeUsernameValidator()],
            },
            "password": {"write_only": True}
            }




"""Reset password for for logged in user"""
class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


"""Manager Serializer"""
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


"""NOTICE SERIALIZER"""
class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


"""SESSION SERIALIZER"""
class SessionYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionYear
        fields = '__all__'






