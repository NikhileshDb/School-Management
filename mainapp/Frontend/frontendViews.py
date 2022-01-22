from django.shortcuts import render
from mainapp.models import Documents, AcademicCalender, Notice
from django.contrib.auth import authenticate, login






def HomePage(request):
    notices = Notice.objects.all()
    context={"notices": notices}
    return render(request, 'templates/Frontend/homePage.html', context)



def AboutPage(request):
    return render(request, 'templates/Frontend/Pages/aboutPage.html')

def ImportandDocs(request):
    docs = Documents.objects.all()
    context = {
        "docs": docs
    }
    return render(request, 'templates/Frontend/Pages/ImportantDocsPage.html', context)

def Holidays(request):
    dates = AcademicCalender.objects.all()
    context = {
        "dates": dates
    }
    return render(request, 'templates/Frontend/Pages/CalenderHolidays.html', context)

student_table_data = [
    {
        "class": "I",
        "boys": 9,
        "girls": 6,
        "total": 15

    },
      {
        "class": "II",
        "boys": 10,
        "girls": 7,
        "total": 17
    },
    {
        "class": "III",
        "boys": 10,
        "girls": 10,
        "total": 20
    },
    {
        "class": "IV",
        "boys": 16,
        "girls": 13,
        "total": 29
    },
      {
        "class": "V",
        "boys": 15,
        "girls": 17,
        "total": 32
    },
      {
        "class": "VI",
        "boys": 19,
        "girls": 15,
        "total": 34
    },
      {
        "class": "VII",
        "boys": 35,
        "girls": 27,
        "total": 62
    },
      {
        "class": "IX",
        "boys": 49,
        "girls": 47,
        "total": 96
    },
      {
        "class": "X",
        "boys": 54,
        "girls": 56,
        "total": 110
    }
]

def StudentTable(request):
    context = {
        "student_table": student_table_data
    }
    return render(request, 'templates/Frontend/Pages/studentTable.html', context)    



def detailedNotice(request, pk):
    obj = Notice.objects.get(notice_id=pk)
    context = {'obj': obj}
    return render(request, 'templates/Frontend/Pages/detailedNotice.html', context)


# def loginPage(request):
#     user_email = request.POST.get('email')
#     password = request.POST.get('password')
#     user = authenticate(email= user_email, password = password)
#     if user is not None:
#         login(request, user)
#         print("User Logged in successfully")
#     else:
#         print('User is not logged in')
#     print(user_email, password)
#     return render(request, 'templates/Frontend/Pages/loginPage.html')