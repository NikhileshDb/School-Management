from rest_framework.viewsets import ModelViewSet
from mainapp.library.serializers import BookSerializer, LibrarySerializer
from mainapp.library.libaryModel import Book, Library
"""Book API for CRUD operations"""
class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer 
    queryset = Book.objects.all()

"""Library API for CRUD operations"""
class LibraryViewSet(ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()

   