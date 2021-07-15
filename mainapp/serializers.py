from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name', 'email', 'password', 'username']


class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class StudentSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    class Meta:
        model = Students
        fields = [
            'id',
            'customuser', 
            'section',
            'middleName',
            'dob',
            'gender',
            'fatherName',
            'motherName',
            'current_address',
            'parmanent_address',
            'religion',
            'phoneNumber',
            'nationality',
            'updated_at',
            'profile_pic',
            'blood_group',
            'classRoom',

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
            motherName = validated_data.pop('motherName'),
            current_address = validated_data.pop('current_address'),
            parmanent_address = validated_data.pop('permanent_address'),
            religion = validated_data.pop('religion'),
            phoneNumber = validated_data.pop('phoneNumber'),
            nationality = validated_data.pop('nationality'),
            updated_at = validated_data.pop('updated_at'),
            profile_pic = validated_data('profile_pic'),
            blood_group = validated_data('blood_group'),
            classRoom = validated_data('classRoom'),
            rollNo = validated_data('rollNo'),
        )

        return student



class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'

