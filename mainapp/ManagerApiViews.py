
from rest_framework.fields import ReadOnlyField
from . serializers import ManagerSerializer, StudentSerializer, TeachersSerializer, PasswordSerializer, ProfileImageSerializer,CustomUserSerializer,classRoomSerializer, SubjectSerializer
from . models import *
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView
from rest_framework import status, filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser, FileUploadParser 


class ProfileImageView(APIView):
    parser_classes = [ FormParser, MultiPartParser, JSONParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = ProfileImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




#Cleaner API For CRUD operation StudentModel
class StudentViewSet(ModelViewSet):
    parser_classes = [JSONParser, FormParser, MultiPartParser ]
    serializer_class = StudentSerializer
    queryset = Students.objects.all()
    # search_fields = ['customuser']
    # filter_backends = (filters.SearchFilter,)
    #Route to change the profile pic
    @action(detail=True, methods=['put'])
    def profile(self,request, pk=None):
        customuser = self.get_object()
        profile = customuser.customuser
        serializer = CustomUserSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Can be used for all Users
class ChangePasswordInstanceView(UpdateAPIView):
    '''Used for update-only endpoints for a single model instance. To Change Password'''
    serializer_class = PasswordSerializer

    #User should be logged in to change password
    permission_classes = [IsAuthenticated]

    #Get the user object from logged in user
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    #Updating the password
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                context = {
                    "old_password": ["Wrong Password."],
                }
                return Response(context,status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                self.object.set_password(serializer.data.get('new_password'))
                self.object.save()
                context = {
                    "status": "success",
                    "code": status.HTTP_200_CREATED,
                    "message": "Password Updated Successfully",
                    "data": []
                }
                return Response(context)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)




#Search for user according to username, name, email
class CustomUserSearch(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['username','email', 'first_name', 'last_name', 'middleName']


class classRoomViewSet(viewsets.ModelViewSet):
    serializer_class = classRoomSerializer
    queryset = classRoom.objects.all()

    

class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


# class student_class(viewsets.APIView):
#     classRoom = SubjectSerializer()
#     def get(self, request, format=None):
#         classes = Students.objects.filter(classRoom=classRoom)