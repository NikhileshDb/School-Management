from rest_framework import serializers
from mainapp.classRoom.classesSubjects import classRoom, section, Subject
from rest_framework.validators import UniqueTogetherValidator
from mainapp.teacher.serailizers import TeacherSerializer
from mainapp.serializers import SessionYearSerializer

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
    



"""Section Serializer"""
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = section
        fields = ('section_id','name','nick_name', 'class_id','teacher')

    """Unique Validators"""
    validators = [
        UniqueTogetherValidator(
            queryset= section.objects.all(),
            fields = ['name','class_id']
        )
    ]
    """Inherits parent Section Serializer"""
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['teacher'] = TeacherSerializer(instance.teacher).data
        response['class_id'] = classRoomSerializer(instance.class_id).data
        return response
    
"""Subject Serializer"""
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

    """Unique Validators"""
    validators = [
        UniqueTogetherValidator(
            queryset= Subject.objects.all(),
            fields = ['class_id', 'subject_name']
        )
    ]

    """Inherits parent Subject Serializer"""
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['class_id'] = classRoomSerializer(instance.class_id).data
        response['teacher'] = TeacherSerializer(instance.teacher).data
        response['session_year'] = SessionYearSerializer(instance.session_year).data
        return response
 
