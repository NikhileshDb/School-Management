"""Required imports for RoutineAPIVieews"""
from .serializers import RoutineSerializer
from rest_framework import viewsets
from .models import ClassRoutine


"""Routine API for CRUD operations"""
class RoutineViewSet(viewsets.ModelViewSet):
    queryset = ClassRoutine.objects.all()
    serializer_class = RoutineSerializer
