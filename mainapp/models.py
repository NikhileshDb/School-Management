"""All the required imports for models"""
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from tinymce.models import HTMLField

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
        ('manager',"Manager"), 
        ('teacher', "Teacher"), 
        ('student', "Student"),
        ('parent', "Parent")
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
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
        )
    notice_id = models.AutoField(primary_key=True)
    notice_title = models.CharField(max_length=100, null=True, blank=True)
    notice = HTMLField(null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=15, blank=True, null=True)

    class Meta:
        ordering = [('-published_at')]
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'
    def __str__(self):
        return self.notice_title


class Documents(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    pdf_file = FilerFileField(null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
    def __str__(self):
        return self.name

class AcademicCalender(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class AddressBook(models.Model):
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    house_no = models.CharField(max_length=100, null=True)
    address_line1 = models.CharField(max_length=200, null=True, blank=True)
    address_line2 = models.CharField(max_length=200, null=True, blank=True)
    pin_code = models.BigIntegerField(null=True, blank=True)
