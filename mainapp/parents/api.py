from mainapp.parents.parentsModel import parent
from mainapp.parents.serializers import parentSerializer
from rest_framework.viewsets import ModelViewSet


"""Parents API for CRUD Operation"""
class parentViewSet(ModelViewSet):
    serializer_class = parentSerializer
    queryset = parent.objects.all()


