from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from mainapp.students.serializers import StudentSerializer, enrollSerializer
from mainapp.students.studentModel import student, enroll


"""Enrollment API for CRUD operations"""
class EnrollmentViewSet(ModelViewSet):
    serializer_class = enrollSerializer
    queryset = enroll.objects.all()



"""Student API for CRUD Operation"""
class StudentViewSet(ModelViewSet):
    parser_classes = [JSONParser, FormParser, MultiPartParser ]
    serializer_class = StudentSerializer
    queryset = student.objects.all()
 #After student object is created, create a enroll object reference with the student instance
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     enroll.objects.create(
    #         enroll_code = instance.student_code,
    #         student = instance,
    #         class_id = instance.class_id,
    #         section = instance.section,
    #         roll = instance.roll,
    #         running_year = instance.running_year,
    #     )
    
    # search_fields = ['customuser']
    # filter_backends = (filters.SearchFilter,)
