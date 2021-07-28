from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    display_fields = ('user.id')

@admin.register(parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('parent_id','customuser', 'phone', 'address', 'profession')

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'customuser','birthday', 'phone')

@admin.register(dormitory)
class DormitoryAdmin(admin.ModelAdmin):
    list_display = ('dormitory_id', 'name', 'number_of_room', 'description')

@admin.register(transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('transport_id', 'route_name', 'number_of_vehicle', 'route_fare')

@admin.register(teacher)
class TeacherAdmin(admin.ModelAdmin):
    display_fields = ('teacher_id', 'customuser.first_name', 'phone','address' )

@admin.register(classRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    display_fields = '__all__'

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    display_fields = '__all__'

admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    display_fields = '__all__'
admin.site.register(ProfileImage)
admin.site.register(StudentResult)
admin.site.register(TestModel)
admin.site.register(SessionYear)
admin.site.register(enroll)
admin.site.register(mark)
admin.site.register(StudentAppearedExam)