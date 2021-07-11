from django.urls import path
from .views import *
from .PrincipalViews import *
from .StudentViews import *
from .TeacherViews import *
from .PrincipalApiViews import *
urlpatterns =[
    path('', index, name="index" ),
    path('add_student/', add_students, name="add_student" ),
    path('student_list/', StudentList, name="student_list"),
    path('add_teacher/', add_teachers, name="add_teacher" ),
    path('teacher_list/', TeacherList, name="teacher_list" ),
]

