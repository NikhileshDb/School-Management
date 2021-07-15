from rest_framework.views import APIView
from . serializers import ManagerSerializer, StudentSerializer, TeachersSerializer, PasswordSerializer
from . models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



#Cleaner API For CRUD operation StudentModel
class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()


# class StudentImageViewSet(APIView):
#     permission_classes = [IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]

#     def post()





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
                return Response(context, status.HTTP_400_BAD_REQUEST)
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
            return Response(serializer.error, status.HTTP_400_BAD_REQUEST)




