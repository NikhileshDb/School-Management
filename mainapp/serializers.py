from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model =Principal
        fields = '__all__'

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'