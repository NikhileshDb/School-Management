
from mainapp.models import CustomUser, Notice, SessionYear, Settings
from mainapp.serializers import CustomUserSerializer, NoticeSerializer, PasswordSerializer, ProfileImageSerializer, SessionYearSerializer, SettingsSerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework import status, filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser



"""Settings API for CRUD Operation"""
class SettingsViewSet(viewsets.ModelViewSet):
    serializer_class = SettingsSerializer
    queryset = Settings.objects.all()


"""Profile API for CRUD Operation"""
class ProfileImageView(APIView):
    parser_classes = [ FormParser, MultiPartParser, JSONParser]

    """Post function for creating Profile and exception handling"""
    def post(self, request, format=None):
        print(request.data)
        serializer = ProfileImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


"""Update/Change Password for all users"""
class ChangePasswordInstanceView(UpdateAPIView):

    '''Used for update-only endpoints for a single model instance. To Change Password'''
    serializer_class = PasswordSerializer

    """This ensures that the user must be logged in to change/update"""
    permission_classes = [IsAuthenticated]

    """Get the user object from logged in user"""
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj


    """This perform password update and notify successful/unsuccessful update message"""
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


""""Custom search for searching user according to username, name, email"""
class CustomUserSearch(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['username','email', 'first_name', 'last_name', 'middleName']


"""Notice API for CRUD operations"""
class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()

"""Session Year API for CRUD operations"""
class SessionYearViewset(viewsets.ModelViewSet):
    serializer_class = SessionYearSerializer
    queryset = SessionYear.objects.all()







