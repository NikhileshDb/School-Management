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

@api_view(['POST'])
def add_students_save(request):
    if request.methode != 'POST':
        content= {
            'Methode Not Allowed':'Your Request is Not Saved'
        }
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)
    else:
        firstName = request.data['firstName']
        middleName = request.data['middleName']
        lastName = request.data['lastName']
        dob = request.data['dob']
        gender = request.data['gender']
        fatherName = request.data['fatherName']
        motherName = request.data['motherName']
        current_address = request.data['current_address']
        parmanent_address = request.data['parmanent_address']
        religion = request.data['religion']
        phoneNumber = request.data['phoneNumber']
        nationality = request.data['nationality']
        created_at = request.data['created_at']
        updated_at = request.data['updated_at']
        profile_pic = request.data['profile_pic']
        blood_group = request.data['blood_group']
        classRoom = request.data['classRoom']
        section = request.data['section']
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        try:
            user = CustomUser.objects.create_user(user_type=3,username=username,email=email, first_name=firstName, last_name=lastName, password = password)
            user.students.middleName = middleName
            user.students.dob = dob
            user.students.gender = gender
            user.students.fatherName = fatherName
            user.students.motherName = motherName
            user.students.current_address = current_address
            user.students.parmanent_address =  parmanent_address
            user.students.religion = religion
            user.students.phoneNumber = phoneNumber
            user.students.nationality = nationality
            user.students.updated_at = updated_at
            user.students.profile_pic = profile_pic
            user.students.blood_group = blood_group
            user.students.classRoom = classRoom
            user.students.section = section
            user.save()
            students = StudentsSerializer(user.students)
            custom = CustomUserSerializer(user)
            data = {
                'custom': custom,
                'students': students
                
            }
            return Response(data)
        except:
            data = {
                "Data Not Saved": "Saving Data Error"
            }
            return Response(status=status.HTTP_401_UNAUTHORIZED)