from rest_framework.viewsets import ModelViewSet
from mainapp.examination.serializers import ExamSerializer, StudentAppearedExamSerialize, StudentResultSerializer, gradeSerializer, markSerializer
from mainapp.examination.examModel import Exam, StudentAppearedExam, StudentResult, grade, mark
from django_filters.rest_framework import DjangoFilterBackend


"""Exam API for CRUD operations"""
class ExamViewSet(ModelViewSet):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


"""Student Appeared API for CRUD operations"""
class StudentAppearedViewSet(ModelViewSet):
    serializer_class = StudentAppearedExamSerialize
    queryset = StudentAppearedExam.objects.all()


"""Grade API for CRUD operations"""
class GradeViewSet(ModelViewSet):
    serializer_class = gradeSerializer
    queryset = grade.objects.all()



"""Mark API for CRUD operations"""
class MarkViewSet(ModelViewSet):
    serializer_class = markSerializer
    queryset = mark.objects.all()


"""Student Result Viewset"""
class StudentResultViewset(ModelViewSet):
    serializer_class = StudentResultSerializer
    queryset = StudentResult.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student', 'subject', 'exam']
    # search_fields = ['student__customuser__username', 'student__customuser__first_name']
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['student__customuser__username', 'subject__classRoom']


