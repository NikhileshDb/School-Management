from django.db import models
from mainapp.models import CustomUser

"""Parents Model"""
class parent(models.Model):
    customuser = models.OneToOneField(CustomUser, on_delete = models.CASCADE, null=True)  #FK
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    mother_occupation = models.CharField(max_length=100, null=True, blank =True)
    parent_id = models.AutoField(primary_key=True)
    phone = models.BigIntegerField(null=True, blank=True)
    address  = models.TextField(null=True, blank=True)
    father_profession = models.CharField(max_length=150,null=True, blank=True)
    family_anuual_income = models.BigIntegerField(null=True, blank=True)
    objects = models.Manager()

   

