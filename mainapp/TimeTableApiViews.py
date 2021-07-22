from .serializers import TimeTableSerializer
from rest_framework import viewsets
from .models import TimeTable

"""handle all the crus function"""

class TimeTableViewSet(viewsets.ModelViewSet):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
