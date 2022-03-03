from rest_framework import serializers
from mainapp.transport.transportModel import transport


"""TRANSPORT SERIALIZER"""
class TransPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = transport
        fields = '__all__'

