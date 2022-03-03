from mainapp.models import CustomUser
from mainapp.students.studentModel import student
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('user_type','profile_pic' ,'username', 'email', 'password1', 'password2')

class EnrollMentForm(ModelForm):
    class Meta:
        fields = '__all__'


class StudentForm(ModelForm):
    class Meta:
        model = student
        fields = '__all__'

