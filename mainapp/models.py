"""All the required imports for models"""
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

"""Session Year Model"""
class SessionYear(models.Model):
    session_id = models.AutoField(primary_key=True)
    running_year = models.DateField(unique=True, default=1)
    objects = models.Manager()
    def __str__(self):
        return str(self.running_year)


"""Settings Model capable of changing skin color"""
class Settings(models.Model):
    color = (
        ('light', 'light'),
        ('dark', 'dark'),
    )
    running_year = models.ForeignKey(SessionYear, on_delete=models.RESTRICT, default=1)
    skin_color = models.CharField(choices=color,max_length=20, default="light")

    def __str__(self):
        return str(self.running_year)


#Overriding Default USER
"""Custom user that overrides Default User"""
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


"""Manager Model"""
class Manager(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    objects = models.Manager()




"""Profile Image Model"""
class ProfileImage(models.Model):
    image = models.ImageField(_("Image"),upload_to="student_profile/", default="media/default.png" , blank=True, null=True )
    desc =  models.CharField(max_length=20, blank=True, null=True)


"""Notice Model"""
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
