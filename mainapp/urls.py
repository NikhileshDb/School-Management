from django.urls import path, include
from .views import *

from .StudentViews import *
from .TeacherViews import *
from .ManagerApiViews import StudentViewSet, ChangePasswordInstanceView,  ProfileImageView, CustomUserSearch, classRoomViewSet, SubjectViewSet
from .TeacherApiViews import StudentResultViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/student', StudentViewSet)
router.register('api/user',CustomUserSearch)
router.register('api/classroom',classRoomViewSet )
router.register('api/subject',SubjectViewSet )
router.register('api/result', StudentResultViewset)
urlpatterns =[
    path('', index, name="index" ),
    path('', include(router.urls)),
    path('api/student/password', ChangePasswordInstanceView.as_view()),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/image/' ,  ProfileImageView.as_view()),
]



