from . models import StudentResult
from rest_framework.viewsets import ModelViewSet
from . serializers import StudentResultSerializer

class StudentResultViewset(ModelViewSet):
    serializer_class = StudentResultSerializer
    queryset = StudentResult.objects.all()
    









