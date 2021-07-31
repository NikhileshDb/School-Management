from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
import uuid
from django.utils.translation import ugettext as tr


class SessionYear(models.Model):
    session_id = models.AutoField(primary_key=True)
    running_year = models.DateField(unique=True, default=1)
    objects = models.Manager()
    def __str__(self):
        return str(self.running_year) #parse_date(self.session_start_year) #str(self.session_start_year) + ' to ' + str(self.session_end_year)


######SETTINGS#######
class Settings(models.Model):
    color = (
        ('light', 'light'),
        ('dark', 'dark'),
    )
    running_year = models.ForeignKey(SessionYear, on_delete=models.RESTRICT, default=1)
    skin_color = models.CharField(choices=color,max_length=20, default="light")
#     running_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return str(self.running_year)


#Overriding Default USER
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

########Manager
class Manager(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    objects = models.Manager()
 

        ######## TEACHER######
class teacher(models.Model):
    customuser = models.OneToOneField(CustomUser, on_delete = models.CASCADE) 
    teacher_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
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
    # def __str__(self):
    #     return self.customuser.username



class classRoom(models.Model):
    class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    name_numeric = models.BigIntegerField(null=True, blank=True)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, default=None)  #FK
    def __str__(self):
        return self.name


"""SECTION"""
class section(models.Model):
    section_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5, null=True, blank=True)
    nick_name = models.CharField(max_length=50, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete=models.CASCADE, default=None, null=True, blank=True)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, default=None, null=True, blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.name

#### PARENT MODEL ###########
class parent(models.Model):
    customuser = models.OneToOneField(CustomUser, on_delete = models.CASCADE, null=True)  #FK
    parent_id = models.AutoField(primary_key=True)
    phone = models.BigIntegerField(null=True, blank=True)
    address  = models.TextField(null=True, blank=True)
    profession = models.CharField(max_length=150,null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.customuser.username
    

class transport(models.Model):
    transport_id = models.AutoField(primary_key=True)
    route_name = models.CharField(max_length=500, null=True, blank=True)
    number_of_vehicle = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    route_fare = models.BigIntegerField(null=True, blank=True)
    def __str__(self):
        return self.route_name

class dormitory(models.Model):
    dormitory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    number_of_room = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

######ENROLL###########
class enroll(models.Model):
    enroll_id = models.AutoField(primary_key=True)
    enroll_code = models.UUIDField(editable=False, default=uuid.uuid4)
    #student = models.ForeignKey(student, on_delete=models.CASCADE, default=None, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE, default=None, null=True, blank=True)
    section = models.ForeignKey(section, on_delete=models.CASCADE, default=None, null=True, blank=True)
    roll = models.BigIntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    running_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE, null=True, blank=True)# default=get_running_year)
    # def __str__(self):
    #     return str(self.enroll_code)

#Set Default Value for for running year in student
# def get_running_year():
#     return Settings.objects.get(id=1)
###### STUDENT MODEL #############
class student(models.Model):
    customuser = models.OneToOneField(CustomUser, on_delete = models.CASCADE)       #FK
    student_id = models.AutoField(primary_key=True)
    # student_code = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(max_length=8, null=True, blank=True)
    sex = models.CharField(max_length=20, null=True, blank=True)
    religion = models.CharField(max_length=20, null=True, blank=True)
    blood_group = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    # roll = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
    enroll = models.OneToOneField(enroll, on_delete = models.CASCADE, default=1)
    # class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE, default=None, null=True, blank=True)#FK
    # section = models.ForeignKey(section, on_delete=models.CASCADE, default=None, null=True, blank=True) #FK
    parent = models.ForeignKey(parent, on_delete=models.CASCADE, default=None, null=True, blank=True)      #FK
    dormitory = models.ForeignKey(dormitory, on_delete=models.CASCADE, default=None, null=True, blank=True)#FK
    transport = models.ForeignKey(transport, on_delete=models.SET_NULL, default=None,null=True, blank=True) #FK
    # running_year = models.ForeignKey(Settings, on_delete=models.CASCADE) #default=get_running_year)  #FK
    class Meta:
        verbose_name_plural = "Students"
    # def __str__(self):
    #     return self.customuser.username




class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, blank=True, null=True)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE, blank=True, default=None)
    objects = models.Manager()
    def __str__(self):
        return self.subject_name

#Testing Image Upload
class ProfileImage(models.Model):
    image = models.ImageField(_("Image"),upload_to="student_profile/", default="media/default.png" , blank=True, null=True )
    desc =  models.CharField(max_length=20, blank=True, null=True)


class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    examName = models.CharField(max_length=50)
    examDate = models.DateField()
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.examName

class StudentAppearedExam(models.Model):
    student_appeared_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default=None, null=True, blank=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE, default=None, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete=models.CASCADE, default=None, null=True, blank=True)
    


class grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5, null=True, blank=True)
    grade_points = models.CharField(max_length=20, null=True, blank=True)
    mark_from = models.BigIntegerField(null=True, blank=True)
    mark_upto = models.BigIntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

class mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE, default=None, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,default=None, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE, default=None, null=True, blank=True)
    section = models.ForeignKey(section, on_delete=models.CASCADE, default=None, null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default=None, null=True, blank=True)
    mark_obtained = models.BigIntegerField(null=True, blank=True)
    mark_total = models.BigIntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE, default=None, null=True, blank=True)


##### THIS IS OBSOLETE ####
class StudentResult(models.Model):
    id = models.AutoField(primary_key=True)
    classRoom = models.ForeignKey(classRoom, on_delete=models.CASCADE, default = None)
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    full_marks = models.FloatField(default=None)
    obtained_marks = models.FloatField(default=None)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



class TestModel(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)



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


class ClassRoutine(models.Model):
    class_routine_id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE)
    section = models.ForeignKey(section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = DayWeekField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE)

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

class Attendance(models.Model):
   
    attendence_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE, default=None, null=True, blank=True)
    class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE, null=True, blank=True)
    section = models.ForeignKey(section, on_delete = models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True



class StudentAttendance(Attendance):
    student = models.ForeignKey(student, on_delete = models.CASCADE)
    class_routine = models.ForeignKey(ClassRoutine, on_delete = models.CASCADE, default=None, null=True, blank=True)

    class Meta:
        abstract = False

class TeacherAttendance(Attendance):
    teacher_id = models.ForeignKey(teacher, on_delete = models.CASCADE)

    class Meta:
        abstract = False
    

class expense_category(models.Model):
    expense_category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class invoice(models.Model):
    status_data = (
        ('paid', 'paid'), 
        ('unpaid', 'unpaid')
    )
    payment_method_data = (
         (1, "Cash"),
        (2, "Cheque"),
        (3, "Online"),
    )
    invoice_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    title = models.CharField(max_length=200),
    description = models.TextField()
    creation_timestamp  = models.DateTimeField()
    amount = models.BigIntegerField()
    amount_paid = models.BigIntegerField()
    due = models.BigIntegerField() #In the view create totalamount - amountpaid
    payment_method = models.CharField(max_length=100, choices=payment_method_data)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices = status_data)
    
#Create Payment as with invoice data

####Payemnt###
class payment(models.Model):
    method_data = (
        (1, "Cash"),
        (2, "Cheque"),
        (3, "Online"),
    )
    payment_id = models.AutoField(primary_key=True)
    expense_category = models.ForeignKey( expense_category , on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    payment_type = models.CharField(max_length = 100, default="Income")
    invoice = models.ForeignKey(invoice, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE, null=True, blank=True)
    method = models.CharField(max_length=100, choices=method_data)
    amount = models.BigIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE)





# class AttendeanceBackUp(models.Model):
#     attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE, null=True, blank=True)
#     status = models.CharField(max_length=30)
#     # student_id = models.ForeignKey(student, on_delete = models.CASCADE)
#     date = models.DateTimeField(auto_now_add=False, auto_now=False)
#     year = models.CharField(max_length=30)
#     class_id = models.ForeignKey(classRoom, on_delete = models.CASCADE)
#     section_id = models.ForeignKey(section, on_delete=models.CASCADE)
#     session = models.ForeignKey(SessionYear, on_delete=models.CASCADE)


