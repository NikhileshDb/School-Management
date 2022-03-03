from rest_framework.viewsets import ModelViewSet
from mainapp.teacher.serailizers import TeacherSerializer
from mainapp.teacher.teacherModel import teacher

"""Teacher API for CRUD operations"""
class teacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset         = teacher.objects.all()

