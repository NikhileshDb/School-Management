from django.shortcuts import render

from mainapp.parents.parentsModel import parent
from .forms import StudentForm, CustomUserForm
from django.forms import inlineformset_factory
from mainapp.students.studentModel import student
from mainapp.models import CustomUser

def Dashboard(request):
    return render(request, 'templates/Backend/pages/dashboard.html')

def Students(request):
    return render(request, 'templates/Backend/pages/students.html')



def settingsPage(request):
    return render(request, 'templates/Backend/pages/settings.html')

def SchoolSettingsPage(request):
    return render(request, 'templates/Backend/pages/schoolSetting.html')


def AddStudent(request):
    customUserForm = CustomUserForm()
    studentDetailsForm = StudentForm()
    # form = inlineformset_factory(CustomUser, student, form = StudentForm, extra=5, can_delete=False)


    context= {
        'customUserForm' : customUserForm,
        'studentDetailsForm': studentDetailsForm,
    }
    return render(request, 'templates/Backend/pages/add_student.html', context)