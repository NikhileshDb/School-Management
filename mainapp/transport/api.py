from rest_framework.viewsets import ModelViewSet
from mainapp.transport.transportModel import transport
from mainapp.transport.serializers import TransPortSerializer


"""Transport API for CRUD operations"""
class TransportViewSet(ModelViewSet):
    serializer_class = TransPortSerializer
    queryset = transport.objects.all()
