from rest_framework import serializers
from mainapp.serializers import CustomUserSerializer
from mainapp.students.studentModel import student, enroll
from mainapp.parents.serializers import parentSerializer
from mainapp.serializers import SessionYearSerializer
from mainapp.classRoom.serializers import classRoomSerializer, SectionSerializer

"""ENROLL SERIALIZER"""
class enrollSerializer(serializers.ModelSerializer):
    class Meta:
        model= enroll
        fields = '__all__'

    """Inherits parent enroll serializer"""
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['running_year'] = SessionYearSerializer(instance.running_year).data
        # response['student'] = StudentSerializer(instance.student).data
        response['class_id'] = classRoomSerializer(instance.class_id).data
        response['section'] = SectionSerializer(instance.section).data
        return response



"""STUDENT SERIALIZER"""
class StudentSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    enroll = enrollSerializer(required=True)
    class Meta:
        model = student
        fields = (
           'student_id','enroll','customuser','birthday', 'sex', 'religion', 'blood_group', 'address', 'phone', 'transport')

    """Overding the create methode serializer"""
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
            transport = validated_data.get('transport'),
            # class_id = validated_data.get('class_id'),
            # section = validated_data.get('section'),
            # roll = validated_data.get('roll')
        )
        return Student

    """Update method does not support writable nested fields by default. 
        So we are overriding update methode explicitly"""
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



