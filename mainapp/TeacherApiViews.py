from . serializers import TeachersSerializer
from .models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status





@api_view(['POST'])
# @permission_classes([IsAdminUser])
def addTeachers(request):
    pass
    # if request.method != 'POST':
    #     content = {
    #         'Method Not Allowed': 'Invalid Request'
    #     }
    #     return Response(content,status=status.HTTP_401_UNAUTHORIZED)
    # else:
    #     name = request.data['name']
    #     admin = request.data['admin']
    #     created_at = request.data['created_at']
    #     updated_at = request.data['updated_at']
    #     objects = request.data['objects']

    #     try:
    #         user = CustomUser.objects.create_user(
    #             user_type=2, 
    #             username=username, 
    #             email=email, 
    #             name=name, 
    #             password=password
    #             )
            
    #         teachers.objects.create(
    #         admin = user,
    #         name = name,
    #         created_at = created_at,
    #         updated_at = updated_at,
    #         objects = objects,
    #         )
    #         data = {
    #             "Saved Successfully": "Teacher added successfully"
    #         }
    #         return Response(data, status=status.HTTP_201_CREATED)
    #     except:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)