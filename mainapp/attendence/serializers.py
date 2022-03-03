from rest_framework import serializers
from mainapp.attendence.attendenceModel import ClassRoutine, Attendance, StudentAttendance, TeacherAttendance
from mainapp.classRoom.serializers import SubjectSerializer, classRoomSerializer, SectionSerializer
from mainapp.serializers import SessionYearSerializer
from rest_framework.validators import UniqueTogetherValidator
from mainapp.students.serializers import StudentSerializer

"""Rouyine Serializer"""
class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoutine
        fields = '__all__'
    
    """Inherits parent Routine Serializer"""
    def to_representation(self, instance):
        response = super(RoutineSerializer, self).to_representation(instance)
        response['subject'] = SubjectSerializer(instance.subject).data
        response['class_id'] = classRoomSerializer(instance.class_id).data
        response['section'] = SectionSerializer(instance.section).data
        response['session_year'] = SessionYearSerializer(instance.session_year).data
        return response


"""Attendance Serializer"""
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


"""Student Attendance Serializer"""
class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'

    """Inherits parent Student Attendance Serializer"""
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['session_year'] = SessionYearSerializer(instance.session_year).data
        response['section'] = SectionSerializer(instance.section).data
        response['class_routine'] = RoutineSerializer(instance.class_routine).data
        response['class_id'] = classRoomSerializer(instance.class_id).data
        response['student'] = StudentSerializer(instance.student).data
        return response

    """Unique Validators"""
    validators = [
        UniqueTogetherValidator(
            queryset = StudentAttendance.objects.all(),
            fields = ['attendence_id', 'student_id', 'class_id', 'status']
        )
    ]



"""Teacher Attendance Serializer"""
class TeacherAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherAttendance
        fields = '__all__'
