from mainapp.attendence.serializers import StudentAttendanceSerializer
from mainapp.serializers import NoticeSerializer
from mainapp.attendence.attendenceModel import ClassRoutine, StudentAttendance
from rest_framework.viewsets import ModelViewSet


"""Routine API for CRUD operations"""
class RoutineViewSet(ModelViewSet):
    queryset = ClassRoutine.objects.all()
    serializer_class = NoticeSerializer


"""Student Attendance API for CRUD operations"""
class StudentAttendanceViewSet(ModelViewSet):
    serializer_class = StudentAttendanceSerializer
    queryset = StudentAttendance.objects.all()



