from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    #Overding the because of password hashing problem in Custom User
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



#Logged in user password reset
class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class StudentSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    class Meta:
        model = Students
        fields = [
            'customuser', 
            'id',
            'classRoom',
            'rollNo',
            'dob',
            'gender',
            'current_address',
            'parmanent_address',
            'fatherName',
            'motherName',
            'religion',
            'phoneNumber',
            'nationality',
            'updated_at',
            'blood_group',
        ]
#Overding the create methode serializer
    def create(self, validated_data):
        customuser_data = validated_data.pop('customuser')
        customuser = CustomUserSerializer.create(
            CustomUserSerializer(), 
            validated_data=customuser_data)


        student, created = Students.objects.update_or_create(
            customuser = customuser,
            dob = validated_data.get('dob'),
            gender = validated_data.get('gender'),
            fatherName = validated_data.get('fatherName'),
            motherName = validated_data.get('motherName'),
            current_address = validated_data.get('current_address'),
            parmanent_address = validated_data.get('permanent_address'),
            religion = validated_data.get('religion'),
            phoneNumber = validated_data.get('phoneNumber'),
            nationality = validated_data.get('nationality'),
            updated_at = validated_data.get('updated_at'),
            blood_group = validated_data.get('blood_group'),
            classRoom = validated_data.get('classRoom'),
            rollNo = validated_data.get('rollNo'),
        )
        return student
#Update method does not support writable nested fields by default. So we are overriding update methode explicitly
    def update(self, instance, validated_data):
        #change 'customuser' here to match your one-to-one field name
        if 'customuser' in validated_data:
            nested_serializer = self.fields['customuser']
            nested_instance = instance.customuser
            nested_data = validated_data.pop('customuser')
            # Runs the update on whatever serializer the nested data belongs to
            nested_serializer.update(nested_instance, nested_data)
        return super(StudentSerializer, self).update(instance, validated_data)
    #To Display the classRoom fields
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['classRoom'] = classRoomSerializer(instance.classRoom).data
        return response





class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'


class classRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = classRoom
        fields = ['standard', 'section']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject_name', 'classRoom']
#To display the classRoom fields,
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['classRoom'] = classRoomSerializer(instance.classRoom).data
        return response
  

class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['subject'] = SubjectSerializer(instance.subject).data
        response['student'] = StudentSerializer(instance.student).data
        return response