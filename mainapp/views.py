from mainapp.payment.paymentModel import invoice, invoice_category, payment
from mainapp.models import SessionYear
from mainapp.students.studentModel import student
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
# @api_view(['GET'])
# def apiOverView(request):
#     api_urls = {
#         'Add Student':      'api/add_student/',
#         'Student List':     'api/student_list',
#         'Add Teacher':      'api/add_teacher',
#         'Teacher List':     'api/teacher_list',
#     }
#     return Response(api_urls)

def index(request):
    students = student.objects.all()
    session_year = SessionYear.objects.all()
    category = invoice_category.objects.all()
    context = {
        'students': students,
        'session_year': session_year,
        'category' : category,
        }
    return render(request, 'add_invoice.html', context)

            
def success(request):
    return render(request, 'success.html')


def save_invoice(request):
    if request.method != 'POST':
        return HttpResponse("Not POST Method")
    else:
        stu_data = request.POST.get('student')
        title = request.POST.get('title')
        description = request.POST.get('description')
        creation_timestamp = request.POST.get('creation_timestamp')
        amount = request.POST.get('amount')
        amount_paid = request.POST.get('amount_paid')
        # due = request.POST.get('due')
        payment_method = request.POST.get('payment_method')
        category = request.POST.get('category')
        session_year = request.POST.get('session_year')
        status = request.POST.get('status')
        
        try:
            #nested_data 
            stu = student.objects.get(customuser__username=stu_data)
            session = SessionYear.objects.get(running_year=session_year)
            category = invoice_category.objects.get(category_name = category)
            #creating instance
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
            invoice_instant = invoice.objects.get(invoice_id=Invoice.invoice_id)

            payment_model = payment.objects.create(title = Invoice.title, description = Invoice.description, payment_type= "income", invoice= invoice_instant, student=Invoice.student, method = Invoice.payment_method, amount=Invoice.amount_paid,timestamp=Invoice.creation_timestamp , session_year = Invoice.session_year, due_from_inv=invoice_instant.due)
            payment_model.save()
            return redirect('success')
        except:
            raise Exception


def invoicehistory(request):
    invoices = invoice.objects.all()
    context = {
        'invoices': invoices,
    }
    return render(request, 'payment_history.html', context)

def paymenthistory(request, pk):
    invoice_obj = invoice.objects.get(invoice_id=pk)
    obj = payment.objects.filter(invoice = pk)

    context = {
        'obj': obj,
        'invoice_obj': invoice_obj,
    }
    return render (request, 'payments.html', context)

def save_update_payments(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        inv_id = request.POST.get('inv_id')
        inv_obj = invoice.objects.get(invoice_id=inv_id)
        method = request.POST.get('payment_method')
        try:
            amount_p = int(inv_obj.amount_paid) + int(amount)
            due_d = int(inv_obj.amount) - int(amount_p)
            inv_obj.amount_paid = amount_p
            inv_obj.due = due_d
            payment_data = payment.objects.create(amount=amount, invoice = inv_obj, method=method, session_year = inv_obj.session_year, due_from_inv = due_d)
            inv_obj.save()
            payment_data.save()
            return redirect('success')
        except:
            raise Exception('Not Saved')
