from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView, name='Home'),
    path('login/',views.LoginView, name='login'),
    path('dataentry/', views.DataEntryView, name='dataentry'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list', views.student_list, name='student_list'),
    path('dataentry/add_employee/', views.add_employee, name='add_employee'),
    path('dataentry/employee_list/', views.employee_list, name='employee_list'),
    path('employee_list/editemployee/<str:pk>/', views.edit_employee, name='editemployee'),
    path('employee_list/delete_employee/<str:pk>/', views.delete_employee, name='delete_employee'),
    path('logout/', views.LogoutView, name='logout'),
    path('editstudent/<str:pk>/', views.EditStudentView, name='editstudent'),
    path('deletestudent/<str:pk>/', views.DeleteStudentView, name='deletestudent'),
]