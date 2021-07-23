
import re
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.validators import UniqueTogetherValidator


####   PROFILE IMAGE SERIALIZER   #####
class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = '__all__'

#####   CUSTOM USER SERIALIZER     #####
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

###############   PARENT SERIALIZER ####################

class parentSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    class Meta:
        model = parent
        fields = ['customuser', 'parent_id', 'phone', 'address','profession', ]
##NESTED DATA SERIALIZER NEED OVERIDE CREATE AND UPDATE METHODE ######
##Overide create method to let customuser be added directly
    def create(self, validated_data):
        customuser_data = validated_data.pop('customuser')
        customuser =  CustomUserSerializer.create(
            CustomUserSerializer() , 
            validated_data = customuser_data
        )
        Parent, created  =  parent.objects.update_or_create(
            customuser = customuser,
            parent_id = validated_data.get('parent_id'),
            phone = validated_data.get('phone'),
            address = validated_data.get('address'),
            profession = validated_data.get('profession'),
        )
        return Parent
###   Override the update Methode #####
    def update(self, instance, validated_data):
        if 'customuser' in validated_data:
            nested_serializer = self.fields['customuser']
            nested_instance = instance.customuser
            nested_data = validated_data.pop('customuser')
            nested_serializer.update(nested_instance, nested_data)
        return super(parentSerializer, self).update(instance, validated_data)




#############     Logged in user password reset    ######################
class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)



class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


"""TEACHER SERIALIZER"""
class TeacherSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    class Meta:
        model = teacher
        fields = '__all__'
    '''Overide The create methode for customuser to add on the parent form'''
    def create(self,validated_data):
        customuser_data = validated_data.pop('customuser')
        customuser = CustomUserSerializer.create(CustomUserSerializer, validated_data=customuser_data)
        Teacher, created = teacher.objects.update_or_create(
            customuser = customuser,
            birthday = validated_data.get('birthday'),
            sex = validated_data.get('sex'),
            religion = validated_data.get('religion'),
            blood_group = validated_data.get('blood_group'),
            address = validated_data.get('address'),
            phone = validated_data.get('phone'),
        )
        return Teacher
   

class classRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = classRoom
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['teacher_id'] = TeacherSerializer(instance.teacher_id).data
        return response
    

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = section
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['teacher_id'] = TeacherSerializer(instance.teacher_id).data
        response['class_id'] = classRoomSerializer(instance.class_id).data
        return response

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        depth=1
 


class StudentResultSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        this_student = validated_data.pop('student')
        this_classroom = validated_data.pop('classRoom')
        obj_student = student.objects.get(customuser__username=this_student)
        obj_classroom = obj_student.classRoom
        if this_classroom != obj_classroom:
            raise ValueError("Value of classroom doesn't matched with students")
        else:
            objects = StudentResult.objects.create(student=this_student,classRoom=this_classroom,**validated_data)
            objects.save()
            return objects

    class Meta:       
        model = StudentResult
        fields = ['id', 'classRoom', 'student','subject', 'full_marks', 'obtained_marks']
        validators = [
            UniqueTogetherValidator(
                queryset = StudentResult.objects.all(),
                fields = ['student', 'subject']
            )
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['subject'] = SubjectSerializer(instance.subject).data
        response['student'] = StudentSerializer(instance.student).data

        response['classRoom'] =classRoomSerializer(instance.classRoom).data
        return response



'''DORMITORY SERIALIZER'''

class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = dormitory
        fields = '__all__'

'''Testing Serilizer functions'''
class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'

'''TRANSPORT SERIALIZER'''
class TransPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = transport
        fields = '__all__'





################ STUDENT SERIALIZER ##############
class StudentSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    classroom = serializers.SlugRelatedField(
        queryset= classRoom.objects.all(),
        slug_field= 'class_id',

    )
    sections = serializers.SerializerMethodField()
    class Meta:
        model = student
        fields = [
            'customuser', 'student_id', 'admission_no', 'birthday', 'sex', 'religion', 'blood_group', 'address', 'phone', 'parent_id', 'dormitory_id', 'transport_id',
            'classroom', 'sections',
        ]
    def get_sections(self, obj):
        sections = section.objects.filter(class_id=obj.classroom)
        return sections

#Overding the create methode serializer
    def create(self, validated_data):
        customuser_data = validated_data.pop('customuser')
        customuser = CustomUserSerializer.create(
            CustomUserSerializer(), 
            validated_data=customuser_data)
        Student, created = student.objects.update_or_create(
            customuser = customuser,
            student_id = validated_data.get('student_id'),
            admission_no = validated_data.get('admission_no'),
            birthday = validated_data.get('birthday'),
            sex = validated_data.get('sex'),
            religion = validated_data.get('religion'),
            blood_group = validated_data.get('blood_group'),
            address = validated_data.get('address'),
            phone = validated_data.get('phone'),
            created_at = validated_data.get('created_at'),
            updated_at = validated_data.get('updated_at'),
            parent_id = validated_data.get('parent_id'),
            dormitory_id = validated_data.get('dormitory_id'),
            transport_id = validated_data.get('transport_id'),
        )
        return Student
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
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['classRoom'] = classRoomSerializer(instance.classRoom).data
    #     return response

        return response


#TimeTable Serializer added by M.J
class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'

