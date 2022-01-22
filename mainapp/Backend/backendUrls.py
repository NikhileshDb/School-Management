from django.urls import path, include
from .backendViews import Dashboard, Students, AddStudent, settingsPage, SchoolSettingsPage

urlpatterns = [
    path('', Dashboard, name="dashboard"),
    path('students/', Students, name="students_page"),
    path('add_student/', AddStudent, name='add_student'),
    path('settings/', settingsPage, name="settings_page"),
    path('school/', SchoolSettingsPage, name="school_settings"),
]