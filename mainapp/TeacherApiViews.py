from . models import StudentResult
from rest_framework.viewsets import ModelViewSet
from . serializers import StudentResultSerializer, TestModelSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class StudentResultViewset(ModelViewSet):
    serializer_class = StudentResultSerializer
    queryset = StudentResult.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student', 'subject', 'exam']
    # search_fields = ['student__customuser__username', 'student__customuser__first_name']
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['student__customuser__username', 'subject__classRoom']
    
class TestView(ModelViewSet):
    serializer_class = TestModelSerializer
    queryset = StudentResult.objects.all()








