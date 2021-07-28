from .serializers import RoutineSerializer
from rest_framework import viewsets
from .models import ClassRoutine

"""handle all the crus function"""

class RoutineViewSet(viewsets.ModelViewSet):
    queryset = ClassRoutine.objects.all()
    serializer_class = RoutineSerializer
