from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView, name='Home'),
    path('login/',views.LoginView, name='login'),
    path('dataentry/', views.DataEntryView, name='dataentry'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list', views.student_list, name='student_list'),
    path('dataentry/employee_list/', views.employee_list, name='employee_list'),
    path('employee_list/add_employee/', views.add_employee, name='add_employee'),
    path('employee_list/editemployee/<str:pk>/', views.edit_employee, name='editemployee'),
    path('employee_list/delete_employee/<str:pk>/', views.delete_employee, name='delete_employee'),
    path('donor_list/', views.donor_list, name='donor_list'),
    path('donor_list/add_donor', views.add_donor,name='add_donor'),
    path('donor_list/edit_donor/<str:pk>/', views.edit_donor,name='edit_donor'),
    path('donor_list/delete_donor/<str:pk>/', views.delete_donor, name='delete_donor'),
    path('dataentry/school_list/',views.school_list, name='school_list'),
    path('school_list/add_school/', views.add_school, name = 'add_school'),
    path('logout/', views.LogoutView, name='logout'),
    path('editstudent/<str:pk>/', views.EditStudentView, name='editstudent'),
    path('deletestudent/<str:pk>/', views.DeleteStudentView, name='deletestudent'),
    path('finance/',views.FinanceView, name='finance'),
    path('donor/',views.DonorView, name='donor'),
]