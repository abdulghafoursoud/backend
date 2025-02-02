from django.urls import path
from crsapp import views
from rest_framework_simplejwt.views import TokenObtainPairView
from crsapp.views import *
from django.urls import re_path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # For logging in
    TokenRefreshView,     # For refreshing the JWT token
)


urlpatterns =[
 #login
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token

   
   
  
#urls for student
    path('Student/',views.manage_Student),
    path('Student/<int:id>/',views.manage_Student),
    path('student-count/', count_students, name='student-count'),
    path('count-diploma-students/', count_diploma_students, name='count_diploma_students'), 
    path('count-degree-students/', count_degree_students, name='count_degree_students'),
    path('Student_Login/', StudentLoginView.as_view(), name='Student_Login'),
    path('Student_Register/', StudentCreateAPIView.as_view(), name='Student_Register'),
    re_path(r'^Student_Reg/(?P<reg_no>.+)/$', get_student_reg, name='get_student_reg'),
    re_path(r'^Student_Update/(?P<reg_no>.+)/$', update_student_info, name='update_student_info'),
    path('check_reg_no/', views.check_reg_no, name='check_reg_no'),
    re_path(r'^check_st_reg_no/(?P<reg_no>.+)/$', check_registration_number, name='check_registration_number'),


#urls for instructor
    path('Instructor_Search_Project/', Instructor_Search_Project, name='Instructor_Search_Project'),
    path('Instructor/',views.manage_Instructor),
    path('Instructor/<int:id>/',views.manage_Instructor),
    path('update_admin_password/<str:email>/', update_admin_password, name='update_admin_password'),
    path('Instructor_Login/', InstructorLoginView.as_view(), name='Instructor_Login'),
    path('Instructor_Email/<str:email>/', views.get_instructor_by_email, name='get_instructor_by_email'),

#urls for project
    path('Project/',views.manage_Project),
    re_path(r'^check_project_reg_number/(?P<st_reg_no>.+)/$', check_project_reg_number, name='check_project_reg_number'),
    path('Project/<int:id>/',views.manage_Project),
    path('project_count/', count_projects, name='project_count'),




]