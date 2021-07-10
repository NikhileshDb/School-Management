from . serializers import TeachersSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(['POST'])
def addTeachers(request):
    if request.method == 'POST':
        try:
            teacher = Teachers.objects.create(
                name = 'name',
                admin = 'admin',
                created_at = 'created_at',
                updated_at = 'updated_at',
                objects = 'objects',
            )
        except:
            return Response(content,status=status.HTTP_401_UNAUTHORIZED)

    serializer = TeachersSerializer(teacher, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listTeachers(request):
    teachers = Teachers.objects.all()

    serializer = TeachersSerializer(teachers, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def updateTeacher(request,pk):
    data = request.data
    update_teacher = Teachers.objects.get(id=pk)
    if request.method == 'PUT':
        try:
            update_teacher.name = request.data['name']
            update_teacher.admin = request.data['admin']
            update_teacher.created_at = request.data['created_at']
            update_teacher.updated_at = request.data['updated_at']
            update_teacher.objects = request.data['objects']

            if update_teacher.is_valid():
                update_teacher.save()
        except:
            return Response(content,status=status.HTTP_401_UNAUTHORIZED)

    serializer = TeachersSerializer(update_teacher, many=False)
    return Response(serializer.data)