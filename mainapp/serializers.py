from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'username']

class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model =Principal
        fields = '__all__'

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    class Meta:
        model = Students
        fields = [
            'customuser', 
            'section', 
            'dob',
            'gender',
        ]
        
    def create(self, validated_data):
        customuser_data = validated_data.pop('customuser')
        customuser = CustomUserSerializer.create(
            CustomUserSerializer(), 
            validated_data=customuser_data)
        student, created = Students.objects.update_or_create(
            customuser = customuser,
            section = validated_data.pop('section'),
            dob = validated_data.pop('dob'),
            gender = validated_data.pop('gender')
        )
        return student