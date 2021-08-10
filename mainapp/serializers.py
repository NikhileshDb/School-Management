from copy import Error
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.validators import UniqueTogetherValidator
import random
from django.utils import timezone

######SESSION SERIALIZER ##########
class SessionYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionYear
        fields = '__all__'


#######SETTINGS SERIALIZER #########
class SettingsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Settings
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['running_year'] = SessionYearSerializer(instance.running_year).data
        return response

####   PROFILE IMAGE SERIALIZER   #####
class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = '__all__'

#####   CUSTOM USER SERIALIZER     #####
class CustomUserSerializer(serializers.ModelSerializer):
    #Overding the because of password hashing problem in Custom User
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
    class Meta:
        model = get_user_model()
        fields = ['id','user_type','first_name', 'last_name', 'middleName','profile_pic', 'email','username', 'password', ]
        extra_kwargs = {
            'username' : {
                'validators': [UnicodeUsernameValidator()],
            },
            "password": {"write_only": True}
            }

###############   PARENT SERIALIZER ####################
# class forSectionSerializer(serializers.Serializer):
#     classroom = serializers.CharField(max_length=50)



class parentSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    class Meta:
        model = parent
        fields = ['customuser', 'parent_id', 'phone', 'address','profession', ]
##NESTED DATA SERIALIZER NEED OVERIDE CREATE AND UPDATE METHODE ######
##Overide create method to let customuser be added directly
    def create(self, validated_data):
        customuser_data = validated_data.pop('customuser')
        customuser =  CustomUserSerializer.create(
            CustomUserSerializer() , 
            validated_data = customuser_data
        )
        Parent, created  =  parent.objects.update_or_create(
            customuser = customuser,
            parent_id = validated_data.get('parent_id'),
            phone = validated_data.get('phone'),
            address = validated_data.get('address'),
            profession = validated_data.get('profession'),
        )
        return Parent
###   Override the update Methode #####
    def update(self, instance, validated_data):
        if 'customuser' in validated_data:
            nested_serializer = self.fields['customuser']
            nested_instance = instance.customuser
            nested_data = validated_data.pop('customuser')
            nested_serializer.update(nested_instance, nested_data)
        return super(parentSerializer, self).update(instance, validated_data)




#############     Logged in user password reset    ######################
class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)



class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


"""TEACHER SERIALIZER"""
class TeacherSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    class Meta:
        model = teacher
        fields = '__all__'
    '''Overide The create methode for customuser to add on the parent form'''
    def create(self,validated_data):
        customuser_data = validated_data.pop('customuser')
        customuser = CustomUserSerializer.create(CustomUserSerializer(), validated_data=customuser_data)
        Teacher, created = teacher.objects.update_or_create(
            customuser = customuser,
            birthday = validated_data.get('birthday'),
            sex = validated_data.get('sex'),
            religion = validated_data.get('religion'),
            blood_group = validated_data.get('blood_group'),
            address = validated_data.get('address'),
            phone = validated_data.get('phone'),
        )
        return Teacher
    '''Update Does not support writable nested fields by default '''
    def update(self, instance, validated_data):
        if 'customuser' in validated_data:
            nested_serializer = self.fields['customuser']
            nested_instance = instance.customuser
            nested_date = validated_data.pop('customuser')
            nested_serializer.update(nested_instance, nested_date)
        return super(TeacherSerializer, self).update(instance, validated_data)



class classRoomSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     class_data = validated_data.get('class_id')
    #     name_data = validated_data.get('name')
    #     name_numeric_data = validated_data.get('name_numeric')
    #     teacher_data = validated_data.get('teacher')
    #     print(class_data)
    #     print(name_data)
    #     print(name_numeric_data)
    #     print(teacher_data)
    #     obj = classRoom.objects.create(**validated_data)
    #     return obj
    class Meta:
        model = classRoom
        fields = ('class_id','name', 'name_numeric', 'teacher')
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['teacher'] = TeacherSerializer(instance.teacher).data
        return response
    

class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = section
        fields = ('section_id','name','nick_name', 'class_id','teacher')

    validators = [
        UniqueTogetherValidator(
            queryset= section.objects.all(),
            fields = ['name','class_id']
        )
    ]
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['teacher'] = TeacherSerializer(instance.teacher).data
        response['class_id'] = classRoomSerializer(instance.class_id).data
        return response
    

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
    validators = [
        UniqueTogetherValidator(
            queryset= Subject.objects.all(),
            fields = ['class_id', 'subject_name']
        )
    ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['class_id'] = classRoomSerializer(instance.class_id).data
        response['teacher'] = TeacherSerializer(instance.teacher).data
        response['session_year'] = SessionYearSerializer(instance.session_year).data
        return response
 


class StudentResultSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        this_student = validated_data.pop('student')
        this_exam = validated_data.pop('exam')
        this_classroom = validated_data.pop('classRoom')
        obj_student = student.objects.get(customuser__username=this_student)
        obj_classroom = obj_student.classRoom
        if this_classroom != obj_classroom:
            raise ValueError("Value of classroom doesn't matched with students")
        else:
            objects = StudentResult.objects.create(student=this_student,classRoom=this_classroom,**validated_data)
            objects.save()
            return objects

    class Meta:
        model = StudentResult
        fields = ['id', 'classRoom', 'student','subject', 'exam', 'full_marks', 'obtained_marks']
        validators = [
            UniqueTogetherValidator(
                queryset = StudentResult.objects.all(),
                fields = ['student', 'subject']
            )
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['subject'] = SubjectSerializer(instance.subject).data
        response['student'] = StudentSerializer(instance.student).data
        response['classRoom'] =classRoomSerializer(instance.classRoom).data
        return response



'''DORMITORY SERIALIZER'''

class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = dormitory
        fields = '__all__'

'''Testing Serilizer functions'''
class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'

'''TRANSPORT SERIALIZER'''
class TransPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = transport
        fields = '__all__'

#####ENROLL SERIALIZER###########

class enrollSerializer(serializers.ModelSerializer):
    class Meta:
        model= enroll
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['running_year'] = SessionYearSerializer(instance.running_year).data
        # response['student'] = StudentSerializer(instance.student).data
        response['class_id'] = classRoomSerializer(instance.class_id).data
        response['section'] = SectionSerializer(instance.section).data
        return response



################ STUDENT SERIALIZER ##############
class StudentSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    enroll = enrollSerializer(required=True)
    class Meta:
        model = student
        fields = (
           'student_id','enroll','customuser','birthday', 'sex', 'religion', 'blood_group', 'address', 'phone','parent', 'dormitory', 'transport',)
#Overding the create methode serializer
    def create(self, validated_data):
        # admission_no = random.randint(1000,1000000)
        enroll_data = validated_data.pop('enroll')
        customuser_data = validated_data.pop('customuser')
        enroll = enrollSerializer.create(enrollSerializer(), validated_data=enroll_data)
        customuser = CustomUserSerializer.create(
            CustomUserSerializer(), 
            validated_data=customuser_data)
        Student, created = student.objects.update_or_create(
            enroll = enroll,
            customuser = customuser,
            # student_code = admission_no,
            birthday = validated_data.get('birthday'),
            sex = validated_data.get('sex'),
            religion = validated_data.get('religion'),
            blood_group = validated_data.get('blood_group'),
            address = validated_data.get('address'),
            phone = validated_data.get('phone'),
            # running_year = validated_data.get('running_year'),
            created_at = validated_data.get('created_at'),
            updated_at = validated_data.get('updated_at'),
            parent = validated_data.get('parent'),
            dormitory = validated_data.get('dormitory'),
            transport = validated_data.get('transport'),
            # class_id = validated_data.get('class_id'),
            # section = validated_data.get('section'),
            # roll = validated_data.get('roll')
        )
        return Student
#Update method does not support writable nested fields by default. So we are overriding update methode explicitly
    def update(self, instance, validated_data):
        #change 'customuser' here to match your one-to-one field name
        if 'customuser' in validated_data:
            nested_serializer = self.fields['customuser']
            nested_instance = instance.customuser
            nested_data = validated_data.pop('customuser')
            # Runs the update on whatever serializer the nested data belongs to
            nested_serializer.update(nested_instance, nested_data)
        if 'enroll' in validated_data:
            nested_serializer = self.fields['enroll']
            nested_data = validated_data.pop('enroll')
            nested_instance = instance.enroll
            nested_serializer.update(nested_instance, nested_data)
        return super(StudentSerializer, self).update(instance, validated_data)
    #To Display the classRoom fields
    def to_representation(self, instance):
        response = super().to_representation(instance)
        # response['class_id'] = classRoomSerializer(instance.class_id).data
        # response['section'] = SectionSerializer(instance.section).data
        # response['enroll'] = enrollSerializer(instance.enroll).data
        response['parent'] = parentSerializer(instance.parent).data
        return response


#TimeTable Serializer added by M.J
class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoutine
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super(RoutineSerializer, self).to_representation(instance)
        response['subject'] = SubjectSerializer(instance.subject).data
        response['class_id'] = classRoomSerializer(instance.class_id).data
        response['section'] = SectionSerializer(instance.section).data
        response['session_year'] = SessionYearSerializer(instance.session_year).data
        return response

####NOTICE SERIALIZER ##########
class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

######SESSION SERIALIZER ##########
class SessionYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionYear
        fields = '__all__'

### GRADE###
class gradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = grade
        fields = '__all__'
##### EXAM SERIALIZER #########
class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['session_year'] = SessionYearSerializer(instance.session_year).data
        return response

##### STUDENT APPEARED #####################
class StudentAppearedExamSerialize(serializers.ModelSerializer):
    def create(self, validated_data):
        this_student = validated_data.get('student')
        this_class = validated_data.get('class_id')
        this_subject = validated_data.get('subject')
        obj_subjects = Subject.objects.filter(class_id__name=this_class)
        

        try:
            obj_subject = obj_subjects.get(subject_name=this_subject)
            
        except:
            raise ValueError("Subject don't exists")

        if this_class != this_student.enroll.class_id:
            raise ValueError("Student doesn't belong to the class")
        elif obj_subject != this_subject:
            raise ValueError("Subjects not matched")
        elif this_student.enroll.class_id != obj_subject.class_id:
             raise ValueError("Subject class and this class don't match")
        else:
            appeared = StudentAppearedExam.objects.create(**validated_data)
            return appeared

    class Meta:
        model = StudentAppearedExam
        fields = '__all__'
    validators = [
        UniqueTogetherValidator(
            queryset= StudentAppearedExam.objects.all(),
            fields = ['student', 'subject','class_id', 'exam']
        )
    ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['exam'] = ExamSerializer(instance.exam).data
        response['subject']  = SubjectSerializer(instance.subject).data
        response['student'] = StudentSerializer(instance.student).data
        response['class_id'] = classRoomSerializer(instance.class_id).data
        return response



####MARK SERIALIZER #########

class markSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        this_student = validated_data.get('student')
        this_class = validated_data.get('class_id')
        this_section = validated_data.get('section')
        this_subject = validated_data.get('subject')
        obj_student = student.objects.get(customuser__username=this_student)
        obj_class = obj_student.enroll.class_id
        obj_section = obj_student.enroll.section
        try:
            appeared_students = StudentAppearedExam.objects.filter(student=obj_student)
        except StudentAppearedExam.DoesNotExist:
            raise ValueError("Student does not exists in the exam")
        else:
            appeared_student = appeared_students.get(subject__subject_name= this_subject)
        if this_student != appeared_student.student:
            raise ValueError("Student not appeared in this exam")
        elif obj_class != this_class and obj_section != this_section:
           raise ValueError("The class and section not matched with the student.")
        else:
            Mark = mark.objects.create(**validated_data)
            return Mark
    class Meta:
        model = mark
        fields = '__all__'
    validators = [
        UniqueTogetherValidator(
            queryset=mark.objects.all(),
            fields=['student','subject',]
        )
    ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
    #     response['session_year'] = SessionYearSerializer(instance.session_year).data
    #     response['student'] = StudentSerializer(instance.student).data
        response['subject'] = SubjectSerializer(instance.subject).data
    #     response['class_id'] = classRoomSerializer(instance.class_id).data
    #     response['section'] = SectionSerializer(instance.section).data
    #     response['exam'] = ExamSerializer(instance.exam).data
        return response




class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['session_year'] = SessionYearSerializer(instance.session_year).data
        response['section'] = SectionSerializer(instance.section).data
        response['class_routine'] = RoutineSerializer(instance.class_routine).data
        response['class_id'] = classRoomSerializer(instance.class_id).data
        response['student'] = StudentSerializer(instance.student).data
        return response
    validators = [
        UniqueTogetherValidator(
            queryset = StudentAttendance.objects.all(),
            fields = ['attendence_id', 'student_id', 'class_id', 'status']
        )
    ]

class TeacherAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherAttendance
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        #We can create our custom creation methode here but we'll use functional view for this
        return invoice.objects.create(**validated_data)

    class Meta:
        model = invoice
        fields = ['invoice_id','title', 'description','creation_timestamp', 'amount','amount_paid', 'payment_method', 'status' , 'student' , 'category', 'session_year']
    
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['student'] = StudentSerializer(instance.student).data
    #     response['session_year'] = SessionYearSerializer(instance.session_year).data
    #     return response

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


    def create(self, validated_data):
        issue_student = validated_data.get('issue_student')
        book_issued = validated_data.get('book_issued')
        issued_date = validated_data.get('issued_date')
        return_date = validated_data.get('return_date')
        try:
            return Library.objects.create(**validated_data)
        except Library.DoesNotExist:
            raise ValueError("library not created")

