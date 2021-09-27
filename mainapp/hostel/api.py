from rest_framework.viewsets import ModelViewSet
from mainapp.hostel.hostelModel import Room, Hostel, RoomAllotment
from mainapp.hostel.serializers import RoomSerializer, HostelSerializer, RoomAllotmentSerializer

"""Dormitory API for CRUD operations"""
class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class HostelViewSet(ModelViewSet):
    serializer_class = HostelSerializer
    queryset = Hostel.objects.all()

class RoomAllotmentViewSet(ModelViewSet):
    serializer_class = RoomAllotmentSerializer
    queryset = RoomAllotment.objects.all()

