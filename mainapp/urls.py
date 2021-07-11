from django.urls import path
from .views import *
from .PrincipalViews import *
from .StudentViews import *
from .TeacherViews import *
from . import TeacherApiViews as views
from . PrincipalApiViews import *
urlpatterns =[
    path('', index, name="index" ),
    

    #Teachers urls
     path('teacher_add/', views.addTeachers, name="add-teacher" ),
    #  path('teacher_list/', views.listTeachers, name="list-teacher" ),
     path('student_add/', add_students_save, name="student_add" ),
     path('student_list/', StudentList, name="student_list"),
]

