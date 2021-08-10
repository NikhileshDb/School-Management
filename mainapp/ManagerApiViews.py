
from django.db.models import query
from rest_framework.fields import ReadOnlyField
from . serializers import *
from . models import *
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView
from rest_framework import status, filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser, FileUploadParser 
from rest_framework import generics



##Settings ViewSet###
class SettingsViewSet(viewsets.ModelViewSet):
    serializer_class = SettingsSerializer
    queryset = Settings.objects.all()

### Parent ViewSet###
class parentViewSet(ModelViewSet):
    serializer_class = parentSerializer
    queryset = parent.objects.all()


#Cleaner API For CRUD operation StudentModel
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

#############   PROFILE IMAGE UPDATE ##############
class ProfileImageView(APIView):
    parser_classes = [ FormParser, MultiPartParser, JSONParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = ProfileImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




#Can be used for all Users
class ChangePasswordInstanceView(UpdateAPIView):
    '''Used for update-only endpoints for a single model instance. To Change Password'''
    serializer_class = PasswordSerializer

    #User should be logged in to change password
    permission_classes = [IsAuthenticated]

    #Get the user object from logged in user
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    #Updating the password
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                context = {
                    "old_password": ["Wrong Password."],
                }
                return Response(context,status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                self.object.set_password(serializer.data.get('new_password'))
                self.object.save()
                context = {
                    "status": "success",
                    "code": status.HTTP_200_CREATED,
                    "message": "Password Updated Successfully",
                    "data": []
                }
                return Response(context)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)




#Search for user according to username, name, email
class CustomUserSearch(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['username','email', 'first_name', 'last_name', 'middleName']


class classRoomViewSet(viewsets.ModelViewSet):
    serializer_class = classRoomSerializer
    queryset = classRoom.objects.all()

class sectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = section.objects.all()

class teacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset         = teacher.objects.all()

class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

class DormitoryViewSet(viewsets.ModelViewSet):
    serializer_class = DormitorySerializer
    queryset = dormitory.objects.all()

class TransportViewSet(viewsets.ModelViewSet):
    serializer_class = TransPortSerializer
    queryset = transport.objects.all()

class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = enrollSerializer
    queryset = enroll.objects.all()

class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()

class SessionYearViewset(viewsets.ModelViewSet):
    serializer_class = SessionYearSerializer
    queryset = SessionYear.objects.all()

class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = gradeSerializer
    queryset = grade.objects.all()

class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = markSerializer
    queryset = mark.objects.all()


class StudentAppearedViewSet(viewsets.ModelViewSet):
    serializer_class = StudentAppearedExamSerialize
    queryset = StudentAppearedExam.objects.all()

class StudentAttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = StudentAttendanceSerializer
    queryset = StudentAttendance.objects.all()


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = invoice.objects.all()


##### Invoice Create ####
@api_view(['POST'])
def add_invoice(request):
    if request.method == 'POST':
        
        serializer = InvoiceSerializer(data = request.data)
        if serializer.is_valid():
            stu_data = request.data.get('student')
            title = request.data.get('title')
            cat = request.data.get('category')
            description = request.data.get('description')
            creation_timestamp = request.data.get('creation_timestamp')
            amount = request.data.get('amount')
            amount_paid = request.data.get('amount_paid')
            payment_method = request.data.get('payment_method')
            session_year = request.data.get('session_year')
            status = request.data.get('status')
            try:
                stu = student.objects.get(customuser__student = stu_data)
                session = SessionYear.objects.get(session_id = session_year)
                category = invoice_category.objects.get(invoice_cat_id = cat)
                #Let's Create the invoice instance first then we will create payment instance with the same data
                Invoice = invoice.objects.create(
                    student = stu,
                    title = title,
                    description = description,
                    creation_timestamp = creation_timestamp,
                    amount = amount, 
                    amount_paid = amount_paid,
                    due = int(amount) - int(amount_paid),
                    payment_method = payment_method,
                    status = status,
                    session_year = session,
                    category = category
                )
                #get the invoice instant
                invoice_instant = invoice.objects.get(invoice_id = Invoice.invoice_id)
                #create the payment instant with reference with the invoice_instant
                payment_model = payment.objects.create(
                    title = Invoice.title, description = Invoice.description, payment_type = "income", invoice = invoice_instant, student = Invoice.student, method = Invoice.payment_method, amount = Invoice.amount_paid, timestamp =Invoice.creation_timestamp, session_year = Invoice.session_year, due_from_inv=invoice_instant.due
                )
                return Response({"Success": "Successfully Created"})
            except:
                return Response({"INVALID": "Not a valid invoice"})
        else:
            return Response({"error":"Serializer Data is not valid"})




## UPDATE INVOICE AND CREATE PAYMENT Instance####
@api_view(['POST'])
def update_invoice_create_payment(request):
    if request.method == 'POST':
        amount = request.data.get('amount')
        inv_id = request.data.get('inv_id')
        inv_obj = invoice.objects.get(invoice_id = inv_id)
        method = request.data.get('method')
        try:    
            amount_p = int(inv_obj.amount_paid) + int(amount)
            due_d = int(inv_obj.amount) - int(amount_p)
            inv_obj.amount_paid = amount_p
            inv_obj.due = due_d
            payment_data = payment.objects.create(amount=amount,invoice = inv_obj, method = method, session_year=inv_obj.session_year, due_from_inv = due_d)
            inv_obj.save() 
            payment_data.save()
            return Response("Success")
        except:
            raise Exception


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = payment.objects.all()


@api_view(['PUT'])
def update_payment(request, pk):
    if request.method == 'PUT':
        serializer = PaymentSerializer(payment,data=request.data)
        try:
            payment_detail = payment.object.update_or_create(amount=amount, invoice = inv_obj, method=method, session_year = inv_obj.session_year)
            payment_detail.save()
            return Response(status=status.is_success())
        except:
            raise Exception('Unsuccessful Attempt')



class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer 
    queryset = Book.objects.all()


class LibraryViewSet(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()

   
