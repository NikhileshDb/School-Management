from django.urls import path
from .backendViews import Dashboard, Students, AddStudent, settingsPage, SchoolSettingsPage, addTeacher, teacherPage, teacherDetail

urlpatterns = [
    path('', Dashboard, name="dashboard"),
    path('students/', Students, name="students_page"),
    path('add_student/', AddStudent, name='add_student'),
    path('settings/', settingsPage, name="settings_page"),
    path('school/', SchoolSettingsPage, name="school_settings"),
    path('add_teacher/', addTeacher, name="add_teacher"),
    path('teachers/', teacherPage, name="manage_teacher"),
    path('teachers/<str:pk>', teacherDetail, name="teacher"),
]