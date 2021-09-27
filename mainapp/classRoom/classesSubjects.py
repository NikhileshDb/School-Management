from django.db import models
from mainapp.teacher.teacherModel import teacher
from mainapp.models import SessionYear
"""Class Room Model"""
class classRoom(models.Model):
    class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    name_numeric = models.BigIntegerField(null=True, blank=True)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, default=None)  #FK
    def __str__(self):
        return self.name


""""Section Model"""
class section(models.Model):
    section_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5, null=True, blank=True)
    nick_name = models.CharField(max_length=50, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete=models.CASCADE, default=None, null=True, blank=True)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, default=None, null=True, blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.name




"""Subject Model"""
class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, blank=True, null=True)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE, blank=True, default=None)
    objects = models.Manager()
    def __str__(self):
        return self.subject_name


