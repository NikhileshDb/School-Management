from django.urls import path
from .views import *
from .PrincipalViews import *
from .StudentViews import *
from .TeacherViews import *
from .PrincipalApiViews import *
urlpatterns =[
    path('', index, name="index" ),
    path('api/', apiOverView, name="api"),
    path('api/add_student/', add_students, name="add_student" ),
    path('api/student_list/', StudentList, name="student_list"),
    path('api/add_teacher/', add_teachers, name="add_teacher" ),
    path('api/teacher_list/', TeacherList, name="teacher_list" ),
]

