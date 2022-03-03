from rest_framework import serializers
from mainapp.hostel.hostelModel import Room, Hostel, RoomAllotment


"""Hostel Serializer"""
class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'

"""Room SERIALIZER"""
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


"""Room Allotment SERIALIZER"""
class RoomAllotmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAllotment
        fields = '__all__'
