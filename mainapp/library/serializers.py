from rest_framework import serializers
from mainapp.library.libaryModel import Book, Library


"""Book Serializer"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

"""Library Serializer"""
class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

    """Function to create Library using validated data and handle exception"""
    def create(self, validated_data):
        issue_student = validated_data.get('issue_student')
        book_issued = validated_data.get('book_issued')
        issued_date = validated_data.get('issued_date')
        return_date = validated_data.get('return_date')
        try:
            return Library.objects.create(**validated_data)
        except Library.DoesNotExist:
            raise ValueError("library not created")

