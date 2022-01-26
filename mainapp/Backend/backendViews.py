from django.shortcuts import render
import json
from mainapp.parents.parentsModel import parent
from .forms import StudentForm, CustomUserForm
from django.forms import inlineformset_factory
from mainapp.students.studentModel import student
from mainapp.models import CustomUser
from mainapp.teacher.teacherModel import teacher
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



def teacherPage(request):
    teacherAll = teacher.objects.all()
 
    context = {
        'teacher': teacherAll,
        
    }
    return render(request, 'templates/Backend/pages/teachers.html', context)
    
def teacherDetail(request, pk):
    singleTeacher = teacher.objects.get(pk=pk)
    context ={
        'singleTeacher': singleTeacher
    }
    return render(request, 'templates/Backend/pages/teachers.html', context)

def addTeacher(request):
    return render(request, 'templates/Backend/pages/add_teacher.html')