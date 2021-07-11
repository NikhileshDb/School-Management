from . serializers import PrincipalSerializer, StudentsSerializer, TeachersSerializer
from . models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import status

#Only Principle Can add New Student
#Only Principle Can Add New Teacher

@api_view(['POST'])
def add_students(request):
    if request.method != 'POST':
        content= {
            'Method Not Allowed':'Your Request is Not Saved'
        }
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)
    else:
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        middleName = request.data['middleName']
        dob = request.data['dob']
        gender = request.data['gender']
        fatherName = request.data['fatherName']
        motherName = request.data['motherName']
        current_address = request.data['current_address']
        parmanent_address = request.data['parmanent_address']
        religion = request.data['religion']
        phoneNumber = request.data['phoneNumber']
        nationality = request.data['nationality']
        updated_at = request.data['updated_at']
        profile_pic = request.data['profile_pic']
        blood_group = request.data['blood_group']
        classRoom = request.data['classRoom']
        section = request.data['section']
        try:
            user = CustomUser.objects.create_user(
                user_type=3,
                username=username,
                email=email, 
                first_name=first_name, 
                last_name=last_name, 
                password = password
                )
            #Creating Students Object With User Details And Password From CustomUser Obj
            Students.objects.create(admin=user,
            middleName = middleName,
            dob = dob,
            gender = gender,
            fatherName = fatherName,
            motherName = motherName,
            current_address = current_address,
            parmanent_address = parmanent_address,
            religion = religion,
            phoneNumber = phoneNumber,
            nationality = nationality,
            updated_at = updated_at,
            profile_pic = profile_pic,
            blood_group = blood_group,
            classRoom = classRoom,
            section = section,
            )
            data = {
                "Successfully Saved": "Student Object is Created"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except:
            data = {
                "Data Not Saved": "Saving Data Error"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def StudentList(request):
    students = Students.objects.all()
    serializer =  StudentsSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAdminUser])
def add_teachers(request):
    if request.method != 'POST':
        content = {
            'Method Not Allowed': 'Invalid Request'
        }
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)
    else:
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        updated_at = request.data['updated_at']
        try:
            user = CustomUser.objects.create_user(
                user_type=2,
                username= username,
                email= email,
                first_name = first_name,
                last_name = last_name,
                password= password,
                )
            
            Teachers.objects.create(
            admin = user,
            updated_at = updated_at,
            )
            data = {
                "Saved Successfully": "Teacher added successfully"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def TeacherList(request):
    obj = Teachers.objects.all()
    serializer = TeachersSerializer(obj, many=True)
    return Response(serializer.data)
