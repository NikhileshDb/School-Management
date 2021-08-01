from django.urls import path, include
from .views import *

from .StudentViews import *
from .TeacherViews import *
from .ManagerApiViews import StudentViewSet, ChangePasswordInstanceView,  ProfileImageView, CustomUserSearch, classRoomViewSet, SubjectViewSet, parentViewSet,  DormitoryViewSet,TransportViewSet, sectionViewSet, teacherViewSet, EnrollmentViewSet, NoticeViewSet, SessionYearViewset , SettingsViewSet, ExamViewSet, GradeViewSet,MarkViewSet, StudentAttendance,StudentAppearedViewSet, StudentAttendanceViewSet
from .TeacherApiViews import StudentResultViewset, TestView
from rest_framework import routers
from .RoutineApiViews import RoutineViewSet

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
urlpatterns =[
    path('success/', success , name="success"),
    path('', index, name="index"),
    path('add_invoice/', add_invoice, name="add_invoice"),
    path('takepayment/', save_update_payments, name="takepayment"),
    path('invoice/', invoicehistory, name="paymenthistory"),
    path('payment/<str:pk>', paymenthistory, name="payments"),
    #####
    path('', include(router.urls)),
    path('api/student/password', ChangePasswordInstanceView.as_view()),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/image/' ,  ProfileImageView.as_view()),
 
]



