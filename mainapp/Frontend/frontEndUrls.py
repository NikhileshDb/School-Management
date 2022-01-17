from django.urls import path, include
from mainapp.Frontend import frontendViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', frontendViews.HomePage),
    path('about-us/', frontendViews.AboutPage, name="about"),
    path('important-docs/', frontendViews.ImportandDocs, name="important_docs"),
    path('calender-holidays/', frontendViews.Holidays, name="calender_holidays"),
    path('students-counter/', frontendViews.StudentTable, name="student_table"),
    # path('login/', frontendViews.loginPage, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('login/', auth_views.LoginView.as_view(template_name='Frontend/Pages/loginPage.html')),
]