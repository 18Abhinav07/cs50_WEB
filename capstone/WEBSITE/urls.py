from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('login_user/<str:user_group>/', views.login_user , name = 'login_user'),
    path('logout_user/', views.logout_user , name = 'logout_user'),
    path('upload_image/<str:user>/', views.upload_image, name='upload_image'),
    
    path('add_non_record/',views.add_non_record , name ='add_non_record'),
    path('add_student_record/',views.add_student_record , name ='add_student_record'),
    
    path('new_user/',views.new_user , name ='new_user'),
    path('register/', views.register, name='register'),
    
    path('student_management/',views.student_management,name='student_management'),
    path('update_student/',views.update_student,name='update_student'),
    
    path('new_student/',views.new_student,name='new_student'),
    path('add_student_details/',views.add_student_details,name='add_student_details'),
    
    path('get_students_data/', views.get_students_data, name='get_students_data'), 
    path('filter_student_records/',views.filter_student_records,name='filter_student_records'),
    
    path('get_details/', views.get_details, name='get_details'), 
    path('check/', views.check, name='check'),
    path('update_student_details/',views.update_student_details, name="update_student_details"),
    
    path('delete_student/', views.delete_student, name = 'delete_student'),
    path('check_r/', views.check_r, name='check_r'),
    path('confirm_delete/', views.confirm_delete, name = 'confirm_delete'),
    
    path('analytics/', views.analytics, name = 'analytics'),
    path('chart_data/', views.chart_data, name ='chart_data'),
    
   
]