from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','first_name', 'last_name', 'middleName', 'email','username', 'password', ]
        extra_kwargs = {
            'username' : {
                'validators': [UnicodeUsernameValidator()],
            }
            }



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
            'section',
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
            'profile_pic',
            'blood_group',
        ]
#Overding the create methodeserializer
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
#Update method does not support writable nested fields by default. So we are overriding update methode explicitly
    def update(self, instance, validated_data):
        #change 'customuser' here to match your one-to-one field name
        if 'customuser' in validated_data:
            nested_serializer = self.fields['customuser']
            nested_instance = instance.customuser
            nested_data = validated_data.pop('customuser')
            # Runs the update on whatever serializer the nested data belongs to
            nested_serializer.update(nested_instance, nested_data)
        # Runs the original parent update(), since the nested fields were
        # "popped" out of the data
        return super(StudentSerializer, self).update(instance, validated_data)





class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'

