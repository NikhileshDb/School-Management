from rest_framework.viewsets import ModelViewSet
from mainapp.hostel.hostelModel import dormitory
from mainapp.hostel.serializers import DormitorySerializer

"""Dormitory API for CRUD operations"""
class DormitoryViewSet(ModelViewSet):
    serializer_class = DormitorySerializer
    queryset = dormitory.objects.all()

