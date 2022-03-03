from mainapp.models import SessionYear
from mainapp.students.studentModel import student
from rest_framework.viewsets import ModelViewSet
from mainapp.payment.serializers import InvoiceSerializer, PaymentSerializer
from mainapp.payment.paymentModel import invoice, invoice_category, payment
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

"""Invoice API for CRUD operations"""
class InvoiceViewSet(ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = invoice.objects.all()


"""Payment API for CRUD operations"""
class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = payment.objects.all()





"""Functions to create Invoice, check validation and notify successful/unsuccessful created message"""
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


                """First create the invoice instance then create payment instance with the same data"""
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
                """Get the invoice instant"""
                invoice_instant = invoice.objects.get(invoice_id = Invoice.invoice_id)

                """create the payment instant with reference with the invoice_instant"""
                payment_model = payment.objects.create(
                    title = Invoice.title, description = Invoice.description, payment_type = "income", invoice = invoice_instant, student = Invoice.student, method = Invoice.payment_method, amount = Invoice.amount_paid, timestamp =Invoice.creation_timestamp, session_year = Invoice.session_year, due_from_inv=invoice_instant.due
                )
                return Response({"Success": "Successfully Created"})
            except:
                return Response({"INVALID": "Not a valid invoice"})
        else:
            return Response({"error":"Serializer Data is not valid"})




"""Functions to update the invoice and create the payment instant"""
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


"""Fuction to update payment and handle exception"""
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

