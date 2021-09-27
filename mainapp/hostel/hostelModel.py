from mainapp.students.studentModel import student
from django.db import models


class Hostel(models.Model):
    name = models.CharField(max_length=20)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    warden = models.CharField(max_length=100, blank=True)
    caretaker = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name



"""Room Model"""
class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy'), ('P', 'Reserved for Research Scholars'),('B', 'Both Single and Double Occupancy')]
    no = models.CharField(max_length=5)
    name = models.CharField(max_length=200,null=True, blank=True)
    room_type = models.CharField(choices=room_choice, max_length=1, default=None)
    vacant = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class RoomAllotment(models.Model):
    student = models.ForeignKey(student, on_delete= models.CASCADE)
    room = models.OneToOneField(
        'Room',
        blank=True,
        on_delete=models.CASCADE,
        null=True)
    room_allotted = models.BooleanField(default=False)
