from rest_framework import serializers
from mainapp.examination.examModel import Exam, StudentAppearedExam, grade, mark, StudentResult
from mainapp.serializers import SessionYearSerializer
from rest_framework.validators import UniqueTogetherValidator
from mainapp.classRoom.classesSubjects import Subject
from mainapp.classRoom.serializers import SubjectSerializer, classRoomSerializer
from mainapp.students.studentModel import student
from mainapp.students.serializers import StudentSerializer


"""SESSION SERIALIZER"""
class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['session_year'] = SessionYearSerializer(instance.session_year).data
        return response





"""Student Appeared Serializer"""
class StudentAppearedExamSerialize(serializers.ModelSerializer):

    """Function to create student appered with validated data and handle errors/exceptions"""
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

    """Unique Validators"""
    validators = [
        UniqueTogetherValidator(
            queryset= StudentAppearedExam.objects.all(),
            fields = ['student', 'subject','class_id', 'exam']
        )
    ]

    """Inherits parent Student Appeared Serializer"""
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['exam'] = ExamSerializer(instance.exam).data
        response['subject']  = SubjectSerializer(instance.subject).data
        response['student'] = StudentSerializer(instance.student).data
        response['class_id'] = classRoomSerializer(instance.class_id).data
        return response



"""Grade SERIALIZER"""
class gradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = grade
        fields = '__all__'




"""MARK SERIALIZER"""
class markSerializer(serializers.ModelSerializer):

    """function to create mark with validated data and handle errors"""
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

    """Unique Validators"""
    validators = [
        UniqueTogetherValidator(
            queryset=mark.objects.all(),
            fields=['student','subject',]
        )
    ]


    """Inherits parent mark serialzer"""
    def to_representation(self, instance):
        response = super().to_representation(instance)
    #     response['session_year'] = SessionYearSerializer(instance.session_year).data
    #     response['student'] = StudentSerializer(instance.student).data
        response['subject'] = SubjectSerializer(instance.subject).data
    #     response['class_id'] = classRoomSerializer(instance.class_id).data
    #     response['section'] = SectionSerializer(instance.section).data
    #     response['exam'] = ExamSerializer(instance.exam).data
        return response





"""Student Result Serializer"""
class StudentResultSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        
        this_student = validated_data.pop('student')
        this_exam = validated_data.pop('exam')
        this_classroom = validated_data.pop('classRoom')
        obj_student = student.objects.get(customuser__username = this_student.customuser.username)
        obj_classroom = obj_student.enroll.class_id
        if this_classroom != obj_classroom:
            raise ValueError("Value of classroom doesn't matched with students")
        else:
            objects = StudentResult.objects.create(student=this_student,classRoom=this_classroom,exam=this_exam,**validated_data)
            objects.save()
            return objects

    class Meta:
        model = StudentResult
        fields = ['id', 'classRoom', 'student','subject', 'exam', 'full_marks', 'obtained_marks']

        """Unique validators"""
        validators = [
            UniqueTogetherValidator(
                queryset = StudentResult.objects.all(),
                fields = ['student', 'subject']
            )
        ]

    """Inherits parent Student Result Serializer"""
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['subject'] = SubjectSerializer(instance.subject).data
        response['student'] = StudentSerializer(instance.student).data
        response['classRoom'] =classRoomSerializer(instance.classRoom).data
        return response

