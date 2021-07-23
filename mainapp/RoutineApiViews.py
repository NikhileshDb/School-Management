from .serializers import RoutineSerializer
from rest_framework import viewsets
from .models import Routine

"""handle all the crus function"""

class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
