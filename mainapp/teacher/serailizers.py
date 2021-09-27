from rest_framework import serializers
from mainapp.serializers import CustomUserSerializer
from mainapp.teacher.teacherModel import teacher



"""TEACHER SERIALIZER"""
class TeacherSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    class Meta:
        model = teacher
        fields = '__all__'

    """Overide The create methode for customuser to add on the parent form"""
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

    """Update Does not support writable nested fields by default"""
    def update(self, instance, validated_data):
        if 'customuser' in validated_data:
            nested_serializer = self.fields['customuser']
            nested_instance = instance.customuser
            nested_date = validated_data.pop('customuser')
            nested_serializer.update(nested_instance, nested_date)
        return super(TeacherSerializer, self).update(instance, validated_data)


