from django.db import models
"""Dormitory Model"""
class dormitory(models.Model):
    dormitory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    number_of_room = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
