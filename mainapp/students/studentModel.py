from django.db import models
from mainapp.models import CustomUser
from mainapp.parents.parentsModel import parent
from mainapp.transport.transportModel import transport
import uuid
from mainapp.classRoom.classesSubjects import classRoom, section
from mainapp.models import SessionYear



"""Enroll Model"""
class enroll(models.Model):
    enroll_id = models.AutoField(primary_key=True)
    enroll_code = models.UUIDField(editable=False, default=uuid.uuid4)
    #student = models.ForeignKey(student, on_delete=models.CASCADE, default=None, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE, default=None, null=True, blank=True)
    section = models.ForeignKey(section, on_delete=models.CASCADE, default=None, null=True, blank=True)
    roll = models.BigIntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    running_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE, null=True, blank=True)# default=get_running_year)
    # def __str__(self):
    #     return str(self.enroll_code)

#Set Default Value for for running year in student
# def get_running_year():
#     return Settings.objects.get(id=1)




'''Student model'''
class student(models.Model):
    customuser = models.OneToOneField(CustomUser, on_delete = models.CASCADE)       #FK
    student_id = models.AutoField(primary_key=True)
    # student_code = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(max_length=8, null=True, blank=True)
    sex = models.CharField(max_length=20, null=True, blank=True)
    religion = models.CharField(max_length=20, null=True, blank=True)
    blood_group = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    # roll = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
    enroll = models.OneToOneField(enroll, on_delete = models.CASCADE, default=1)
    # class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE, default=None, null=True, blank=True)#FK
    # section = models.ForeignKey(section, on_delete=models.CASCADE, default=None, null=True, blank=True) #FK
    parent = models.ForeignKey(parent, on_delete=models.CASCADE, default=None, null=True, blank=True)      #FK
    transport = models.ForeignKey(transport, on_delete=models.SET_NULL, default=None,null=True, blank=True) #FK
    # running_year = models.ForeignKey(Settings, on_delete=models.CASCADE) #default=get_running_year)  #FK
   
    class Meta:
        verbose_name_plural = "Students"
    # def __str__(self):
    #     return self.customuser.username


