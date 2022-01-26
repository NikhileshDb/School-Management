from rest_framework import serializers
from mainapp.parents.parentsModel import parent
from mainapp.serializers import CustomUserSerializer


"""PARENT SERIALIZER"""
class parentSerializer(serializers.ModelSerializer):
    customuser = CustomUserSerializer(required=True)
    class Meta:
        model = parent
        fields = ['customuser', 'parent_id', 'phone', 'address', ]


    """NESTED DATA SERIALIZER NEED OVERIDE CREATE AND UPDATE METHODE"""
    """Overide create method to let customuser be added directly"""
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
        )
        return Parent

    """Override the update Method"""
    def update(self, instance, validated_data):
        if 'customuser' in validated_data:
            nested_serializer = self.fields['customuser']
            nested_instance = instance.customuser
            nested_data = validated_data.pop('customuser')
            nested_serializer.update(nested_instance, nested_data)
        return super(parentSerializer, self).update(instance, validated_data)



