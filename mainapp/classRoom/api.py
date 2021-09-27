from mainapp.classRoom.classesSubjects import Subject, classRoom, section
from mainapp.classRoom.serializers import SectionSerializer, SubjectSerializer, classRoomSerializer
from rest_framework.viewsets import ModelViewSet

"""Class Room API for CRUD operations"""
class classRoomViewSet(ModelViewSet):
    serializer_class = classRoomSerializer
    queryset = classRoom.objects.all()

"""Section API for CRUD Operations"""
class sectionViewSet(ModelViewSet):
    serializer_class = SectionSerializer
    queryset = section.objects.all()

"""Subject API for CRUD operations"""
class SubjectViewSet(ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

