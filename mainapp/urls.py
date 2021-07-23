from django.urls import path, include
from .views import *

from .StudentViews import *
from .TeacherViews import *
from .ManagerApiViews import StudentViewSet, ChangePasswordInstanceView,  ProfileImageView, CustomUserSearch, classRoomViewSet, SubjectViewSet, parentViewSet,  DormitoryViewSet,TransportViewSet, sectionViewSet, teacherViewSet, EnrollmentViewSet
from .TeacherApiViews import StudentResultViewset, TestView
from rest_framework import routers
from .TimeTableApiViews import TimeTableViewSet

router = routers.DefaultRouter()
router.register('api/parent', parentViewSet)
router.register('api/student', StudentViewSet)
router.register('api/user',CustomUserSearch)
router.register('api/class',classRoomViewSet )
router.register('api/subject',SubjectViewSet )
router.register('api/result', StudentResultViewset)
router.register('api/testing', TestView)
router.register('api/dormitory', DormitoryViewSet)
router.register('api/transport',TransportViewSet )
router.register('api/section', sectionViewSet)
router.register('api/teacher',teacherViewSet )
router.register('api/enroll', EnrollmentViewSet)

router.register('api/timetable', TimeTableViewSet)

urlpatterns =[
    path('', index, name="index" ),
    path('', include(router.urls)),
    path('api/student/password', ChangePasswordInstanceView.as_view()),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/image/' ,  ProfileImageView.as_view()),
 
]



