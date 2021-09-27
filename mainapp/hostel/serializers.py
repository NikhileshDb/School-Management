from rest_framework import serializers
from mainapp.hostel.hostelModel import dormitory

"""DORMITORY SERIALIZER"""
class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = dormitory
        fields = '__all__'
