from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Students)
admin.site.register(CustomUser)
admin.site.register(Teachers)
admin.site.register(Subject)
admin.site.register(classRoom)
admin.site.register(StudentResult)