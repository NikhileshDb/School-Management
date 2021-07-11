from . serializers import PrincipalSerializer, StudentsSerializer, TeachersSerializer
from . models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import status

def apiOverView(request):
    api_urls = {

        
    }

#Only Principle Can add New Student
#Only Principle Can Add New Teacher

@api_view(['POST'])
def add_students_save(request):
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

    # {
    #     "id": 2,
    #     "middleName": "My Mid",
    #     "dob": null,
    #     "gender": null,
    #     "fatherName": null,
    #     "motherName": null,
    #     "current_address": null,
    #     "parmanent_address": null,
    #     "religion": null,
    #     "phoneNumber": null,
    #     "nationality": null,
    #     "created_at": "2021-07-11T14:43:00.674484Z",
    #     "updated_at": null,
    #     "profile_pic": null,
    #     "blood_group": null,
    #     "classRoom": null,
    #     "section": null,
    #     "admin": 5
    # }
    #edited


@api_view(['POST'])
# @permission_classes([IsAdminUser])
def addTeachers(request):
    pass
    if request.method != 'POST':
        content = {
            'Method Not Allowed': 'Invalid Request'
        }
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)
    else:
        name = request.data['name']
        admin = request.data['admin']
        created_at = request.data['created_at']
        updated_at = request.data['updated_at']
        # objects = request.data['objects']

        try:
            user = CustomUser.objects.create_user(
                user_type=2,
                username=username,
                email=email,
                name=name,
                password=password,
                )
            
            teachers.objects.create(
            admin = user,
            name = name,
            created_at = created_at,
            updated_at = updated_at,
            objects = objects,
            )
            data = {
                "Saved Successfully": "Teacher added successfully"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)