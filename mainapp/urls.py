"""Required imports for App urls"""
from django.urls import path, include
from .views import *
from .StudentViews import *
from .TeacherViews import *
from .ManagerApiViews import *
from .TeacherApiViews import StudentResultViewset, TestView
from rest_framework import routers
from .RoutineApiViews import RoutineViewSet


"""Routers for all the API functions"""
router = routers.DefaultRouter()
router.register('api/parent', parentViewSet)
router.register('api/student', StudentViewSet)
router.register('api/user',CustomUserSearch)
router.register('api/class',classRoomViewSet )
router.register('api/subject',SubjectViewSet )
router.register('api/exam', ExamViewSet)
router.register('api/result', StudentResultViewset)
router.register('api/testing', TestView)
router.register('api/dormitory', DormitoryViewSet)
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
    path('', index, name="index"),
    path('add_invoice/', save_invoice, name="save_invoice"),
    path('takepayment/', save_update_payments, name="takepayment"),
    path('invoice/', invoicehistory, name="paymenthistory"),
    path('payment/<str:pk>', paymenthistory, name="payments"),

    path('', include(router.urls)),
    path('api/student/password', ChangePasswordInstanceView.as_view()),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/image/' ,  ProfileImageView.as_view()),
    path('api/add-invoice/', add_invoice),
    path('api/payment-update',  update_invoice_create_payment),

]



