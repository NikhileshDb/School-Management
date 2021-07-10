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
     path('teacher/add/', views.addTeachers, name="add-teacher" ),
     path('teacher/list/', views.listTeachers, name="list-teacher" ),
     path('student_add/', add_students_save, name="student_add" ),
     path('teacher/update/', views.updateTeacher, name="update-teacher" ),
]

