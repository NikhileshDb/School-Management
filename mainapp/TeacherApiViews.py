from . models import StudentResult
from rest_framework.viewsets import ModelViewSet
from . serializers import StudentResultSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class StudentResultViewset(ModelViewSet):
    serializer_class = StudentResultSerializer
    queryset = StudentResult.objects.all()
    # filter_backends = (filters.SearchFilter)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subject__subject_name','student__customuser__username',]
    # search_fields = ['student__customuser__username', 'student__customuser__first_name']
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['student__customuser__username', 'subject__classRoom']
    









