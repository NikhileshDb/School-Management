from mainapp.students.studentModel import student
from django.db import models


"""Book Model"""
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=40)
    ISBN = models.CharField(max_length=40)
    publication = models.CharField(max_length=40) 


"""Library Model"""
class Library(models.Model):
    issue_student = models.ForeignKey(student, on_delete=models.CASCADE)
    book_issued = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    issued = models.BooleanField(default=False)

