from django.db import models
from mainapp.models import CustomUser



"""Teacher Model"""
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

