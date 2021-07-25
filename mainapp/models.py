from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
import uuid


#Overriding Default USER
class CustomUser(AbstractUser):
    data = (
        (1,"Manager"), 
        (2, "Teachers"), 
        (3, "Students"),
        (4, "Parent")
    )
    middleName = models.CharField(max_length=15, null=True, blank=True)
    profile_pic = models.ImageField(_("Image"),upload_to='profile_pic/', default="media/default.png" , null=True, blank=True)
    user_type = models.CharField(default=1, choices=data, max_length=20)

class SessionYear(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    objects = models.Manager()
    def __str__(self):
        return str(self.session_start_year) #parse_date(self.session_start_year) #str(self.session_start_year) + ' to ' + str(self.session_end_year)

class Manager(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    objects = models.Manager()
 

        
class teacher(models.Model):
    customuser = models.OneToOneField(CustomUser, on_delete = models.CASCADE) 
    teacher_id = models.AutoField(primary_key=True)
    birthday = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    religion = models.CharField(max_length=30, null=True, blank=True)
    blood_group = models.CharField(max_length=5, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Teachers"
    def __str__(self):
        return self.customuser.username



class classRoom(models.Model):
    class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    name_numeric = models.BigIntegerField(null=True, blank=True)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, default=None)  #FK
    def __str__(self):
        return self.name
    # section_choice = (
    #  ("A","A"),
    #  ("B","B"),
    #  ("C","C"),
    #  ("D","D"),
    # )
    # id = models.AutoField(primary_key=True)
    # standard = models.BigIntegerField(null=True, blank=True)
    # section = models.CharField(choices=section_choice, max_length=1, default='A')
  
    # class Meta:
    #     unique_together =('standard', 'section' )
    # def __str__(self):
    #     return str(self.standard) + ' ' + self.section


"""SECTION"""
class section(models.Model):
    section_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5, null=True, blank=True)
    nick_name = models.CharField(max_length=50, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete=models.CASCADE, default=None, null=True, blank=True)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, default=None, null=True, blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.name

#### PARENT MODEL ###########
class parent(models.Model):
    customuser = models.OneToOneField(CustomUser, on_delete = models.CASCADE, null=True)  #FK
    parent_id = models.AutoField(primary_key=True)
    phone = models.BigIntegerField(null=True, blank=True)
    address  = models.TextField(null=True, blank=True)
    profession = models.CharField(max_length=150,null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.customuser.username
    

class transport(models.Model):
    transport_id = models.AutoField(primary_key=True)
    route_name = models.CharField(max_length=500, null=True, blank=True)
    number_of_vehicle = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    route_fare = models.BigIntegerField(null=True, blank=True)
    def __str__(self):
        return self.route_name

class dormitory(models.Model):
    dormitory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    number_of_room = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

###### STUDENT MODEL #############
class student(models.Model):
    customuser = models.OneToOneField(CustomUser, on_delete = models.CASCADE)       #FK
    student_id = models.AutoField(primary_key=True)
    student_code = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(max_length=8, null=True, blank=True)
    sex = models.CharField(max_length=20, null=True, blank=True)
    religion = models.CharField(max_length=20, null=True, blank=True)
    blood_group = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    roll = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE, default=None, null=True, blank=True)#FK
    section = models.ForeignKey(section, on_delete=models.CASCADE, default=None, null=True, blank=True) #FK
    parent = models.ForeignKey(parent, on_delete=models.CASCADE, default=None, null=True, blank=True)      #FK
    dormitory = models.ForeignKey(dormitory, on_delete=models.CASCADE, default=None, null=True, blank=True)#FK
    transport = models.ForeignKey(transport, on_delete=models.SET_NULL, default=None,null=True, blank=True) #FK
    session = models.ForeignKey(SessionYear, on_delete=models.CASCADE, default=None)  #FK
    class Meta:
        verbose_name_plural = "Students"
    def __str__(self):
        return self.customuser.first_name


######SETTINGS#######

######ENROLL###########
class enroll(models.Model):
    enroll_id = models.AutoField(primary_key=True)
    enroll_code = models.CharField(max_length=100, default=None )
    student = models.ForeignKey(student, on_delete=models.CASCADE, default=None, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE, default=None, null=True, blank=True)
    section = models.ForeignKey(section, on_delete=models.CASCADE, default=None, null=True, blank=True)
    roll = models.BigIntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(SessionYear, on_delete=models.CASCADE, null=True, blank=True, default=None)
    def __str__(self):
        return str(self.enroll_code)

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete=models.CASCADE, blank=True, null=True)
    teacher_id = models.ForeignKey(teacher, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.subject_name

#Testing Image Upload
class ProfileImage(models.Model):
    image = models.ImageField(_("Image"),upload_to="student_profile/", default="media/default.png" , blank=True, null=True )
    desc =  models.CharField(max_length=20, blank=True, null=True)

class StudentResult(models.Model):
    id = models.AutoField(primary_key=True)
    classRoom = models.ForeignKey(classRoom, on_delete=models.CASCADE, default = None)
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    full_marks = models.FloatField(default=None)
    obtained_marks = models.FloatField(default=None)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)




class TestModel(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Routine(models.Model):
    id = models.AutoField(primary_key=True)
    class_room = models.ForeignKey(classRoom, on_delete = models.CASCADE)
    day = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    period = models.CharField(max_length=20)


class Notice(models.Model):
    data = (
        (1, 'Yes'),
        (0, 'No')
    )
    notice_id = models.AutoField(primary_key=True)
    notice_title = models.CharField(max_length=100, null=True, blank=True)
    notice = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    status = models.CharField(choices=data,max_length=10, blank=True, null=True)

class attendence(models.Model):
    attendence_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)