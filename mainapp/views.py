from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    return render(request, 'index.html')

def add_invoice(request):
    return render(request, 'add_invoice.html')