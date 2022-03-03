from mainapp.classRoom.classesSubjects import Subject, classRoom, section
from django.db import models
from mainapp.models import SessionYear
from mainapp.students.studentModel import student



"""Exam Model"""
class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    examName = models.CharField(max_length=50)
    examDate = models.DateField()
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.examName


"""Student Appeared Exam Model"""
class StudentAppearedExam(models.Model):
    student_appeared_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default=None, null=True, blank=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE, default=None, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete=models.CASCADE, default=None, null=True, blank=True)
    

"""Grade Model"""
class grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5, null=True, blank=True)
    grade_points = models.CharField(max_length=20, null=True, blank=True)
    mark_from = models.BigIntegerField(null=True, blank=True)
    mark_upto = models.BigIntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)



"""Mark Model"""
class mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE, default=None, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,default=None, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE, default=None, null=True, blank=True)
    section = models.ForeignKey(section, on_delete=models.CASCADE, default=None, null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default=None, null=True, blank=True)
    mark_obtained = models.BigIntegerField(null=True, blank=True)
    mark_total = models.BigIntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE, default=None, null=True, blank=True)


"""Student Model"""
class StudentResult(models.Model):
    id = models.AutoField(primary_key=True)
    classRoom = models.ForeignKey(classRoom, on_delete=models.CASCADE, default = None)
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    full_marks = models.FloatField(default=None)
    obtained_marks = models.FloatField(default=None)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)