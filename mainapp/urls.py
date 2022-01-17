"""Required imports for App urls"""
from django.urls import path, include
from .views import *
from .ApiViews import *
from rest_framework import routers
from mainapp.parents.api import parentViewSet
from mainapp.students.api import StudentViewSet, EnrollmentViewSet
from mainapp.classRoom.api import classRoomViewSet, SubjectViewSet, sectionViewSet
from mainapp.examination.api import ExamViewSet, StudentResultViewset, GradeViewSet, MarkViewSet, StudentAppearedViewSet

from mainapp.transport.api import TransportViewSet
from mainapp.teacher.api import teacherViewSet
from mainapp.attendence.api import RoutineViewSet, StudentAttendanceViewSet
from mainapp.payment.api import InvoiceViewSet, PaymentViewSet, add_invoice, update_invoice_create_payment
from mainapp.library.api import LibraryViewSet, BookViewSet
from mainapp.hostel.api import RoomViewSet, HostelViewSet, RoomAllotmentViewSet

"""Routers for all the API functions"""
router = routers.DefaultRouter()
router.register('api/parent', parentViewSet)
router.register('api/student', StudentViewSet)
router.register('api/user',CustomUserSearch)
router.register('api/class',classRoomViewSet )
router.register('api/subject',SubjectViewSet )
router.register('api/exam', ExamViewSet)
router.register('api/result', StudentResultViewset)
router.register('api/room', RoomViewSet)
router.register('api/hostel', HostelViewSet)
router.register('api/room-allotment', RoomAllotmentViewSet)

router.register('api/transport',TransportViewSet )
router.register('api/section', sectionViewSet)
router.register('api/teacher',teacherViewSet )
router.register('api/notice',NoticeViewSet )
router.register('api/enroll', EnrollmentViewSet)
router.register('api/sessionyear',SessionYearViewset )
router.register('api/setting', SettingsViewSet)
# router.register('api/timetable', TimeTableViewSet)

router.register('api/routine', RoutineViewSet)
router.register('api/grade', GradeViewSet)
router.register('api/mark', MarkViewSet)
router.register('api/studentattendance', StudentAttendanceViewSet)
router.register('api/studentappeared', StudentAppearedViewSet)
router.register('api/invoice', InvoiceViewSet)
router.register('api/payment', PaymentViewSet)
router.register('api/books', BookViewSet)
router.register('api/library', LibraryViewSet)
urlpatterns =[
    path('success/', success , name="success"),
    path('index/', index, name="index"),
    path('add_invoice/', save_invoice, name="save_invoice"),
    path('takepayment/', save_update_payments, name="takepayment"),
    path('invoice/', invoicehistory, name="paymenthistory"),
    path('payment/<str:pk>', paymenthistory, name="payments"),

    path('api_root/', include(router.urls)),
    path('api/student/password', ChangePasswordInstanceView.as_view()),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/image/' ,  ProfileImageView.as_view()),
    path('api/add-invoice/', add_invoice),
    path('api/payment-update',  update_invoice_create_payment),

]



