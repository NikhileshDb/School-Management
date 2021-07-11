from . serializers import PrincipalSerializer
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
    students = Students.Objects.all()
    serializer =  StudentsSerializer(students, many=True)
    return Response(serializer.data)
