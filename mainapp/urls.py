from django.urls import path, include
from .views import *

from .StudentViews import *
from .TeacherViews import *
<<<<<<< HEAD
from .ManagerApiViews import StudentViewSet, ChangePasswordInstanceView,  ProfileImageView, CustomUserSearch, classRoomViewSet, SubjectViewSet, parentViewSet,  DormitoryViewSet,TransportViewSet, sectionViewSet, teacherViewSet, EnrollmentViewSet, NoticeViewSet, SessionYearViewset , SettingsViewSet
=======
from .ManagerApiViews import StudentViewSet, ChangePasswordInstanceView,  ProfileImageView, CustomUserSearch, classRoomViewSet, SubjectViewSet, parentViewSet,  DormitoryViewSet,TransportViewSet, sectionViewSet, teacherViewSet, EnrollmentViewSet, NoticeViewSet, SessionYearViewset, ExamViewSet
>>>>>>> 3765518de16d5ab2a3e14e3225630595539b4662
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
<<<<<<< HEAD
router.register('api/setting', SettingsViewSet)
# router.register('api/timetable', TimeTableViewSet)
=======
>>>>>>> 3765518de16d5ab2a3e14e3225630595539b4662

router.register('api/routine', RoutineViewSet)


urlpatterns =[
    path('', index, name="index" ),
    path('', include(router.urls)),
    path('api/student/password', ChangePasswordInstanceView.as_view()),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/image/' ,  ProfileImageView.as_view()),
 
]



