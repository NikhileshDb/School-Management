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
            'middleName',
            'section', 
            'dob',
            'gender',
            'fatherName',
            'motherName',
            'current_address',
            'parmanent_address',
            'religion',
            'phoneNumber',
            'nationality',
            'created_at',
            'updated_at',
            'profile_pic',
            'blood_group',
            'classRoom',
            'objects',

        ]
        
    def create(self, validated_data):
        customuser_data = validated_data.pop('customuser')
        customuser = CustomUserSerializer.create(
            CustomUserSerializer(), 
            validated_data=customuser_data)
        student, created = Students.objects.update_or_create(
            customuser = customuser,
            middleName = validated_data.pop('middleName'),
            section = validated_data.pop('section'),
            dob = validated_data.pop('dob'),
            gender = validated_data.pop('gender'),
            fatherName = validated_data.pop('fatherName'),
            motherName = valdated_data.pop('motherName'),
            current_address = validated_data.pop('current_address'),
            parmanent_address = validated_data.pop('permanent_address'),
            religion = validated_data.pop('religion'),
            phoneNumber = validated_data.pop('phoneNumber'),
            nationality = validated_data.pop('nationality'),
            created_at = validated_data.pop('created_at'),
            updated_at = validated_data.pop('updated_at'),
            profile_pic = validated_data('profile_pic'),
            blood_group = validated_data('blood_group'),
            classRoom = validated_data('classRoom'),
            objects = validated_data('objects'),
            
        )
        return student