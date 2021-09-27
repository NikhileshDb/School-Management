from django.db import models
from mainapp.models import CustomUser

"""Parents Model"""
class parent(models.Model):
    customuser = models.OneToOneField(CustomUser, on_delete = models.CASCADE, null=True)  #FK
    parent_id = models.AutoField(primary_key=True)
    phone = models.BigIntegerField(null=True, blank=True)
    address  = models.TextField(null=True, blank=True)
    profession = models.CharField(max_length=150,null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.customuser.username
    
