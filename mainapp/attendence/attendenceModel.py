from django.db import models
from django.utils.translation import ugettext as tr
from mainapp.classRoom.classesSubjects import classRoom, Subject, section
from mainapp.models import SessionYear
from mainapp.students.studentModel import student
from mainapp.teacher.teacherModel import teacher

DAY_OF_THE_WEEK = {
    '1': tr(u'Monday'),
    '2': tr(u'Tuesday'),
    '3': tr(u'Wednesday'),
    '4': tr(u'Thursday'),
    '5': tr(u'Friday'),
    '6': tr(u'Saturday'),
    '7': tr(u'Sunday'),
}
class DayWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] =tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length'] = 1
        super(DayWeekField, self).__init__(*args, **kwargs)


"""Class Model Routine"""
class ClassRoutine(models.Model):
    class_routine_id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE)
    section = models.ForeignKey(section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = DayWeekField(null=True, blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE)




"""Attendance Model"""
class Attendance(models.Model):
    attendence_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE, default=None, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE, null=True, blank=True)
    section = models.ForeignKey(section, on_delete = models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True


"""Student Attendance that inherrites Attendance Model"""
class StudentAttendance(Attendance):
    student = models.ForeignKey(student, on_delete = models.CASCADE)
    class_routine = models.ForeignKey(ClassRoutine, on_delete = models.CASCADE, default=None, null=True, blank=True)

    class Meta:
        abstract = False


"""Teacher Attendance that inherrites Attendance Model"""
class TeacherAttendance(Attendance):
    teacher_id = models.ForeignKey(teacher, on_delete = models.CASCADE)

    class Meta:
        abstract = False
    