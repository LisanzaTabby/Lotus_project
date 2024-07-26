import django_filters
from django_filters import *
from .models import Student, Employee

class StudentFilter(django_filters.FilterSet):
    GENDER = (
        ('Female','Female'),
        ('Male', 'Male')
    )
    LEVELOFSTUDY = (
        ('Primary','Primary'),
        ('Secondary','Secondary'),
        ('Tertiary','Tertiary'),
    )
    name = CharFilter(field_name='firstname', lookup_expr='icontains', label='Student name')
    gender = ChoiceFilter(choices = GENDER)
    levelofstudy = ChoiceFilter(choices=LEVELOFSTUDY)

    class Meta:
        model =  Student
        fields= ['gender']

class EmployeeFilter(django_filters.FilterSet):
    GENDER = (
        ('Female','Female'),
        ('Male','Male'),
    )
    DEPT =(
        ('Finance', 'Finance'),
        ('Records', 'Records'),
        ('Research', 'Research'),
        ('HR', 'HR'),
    )
    name = CharFilter(field_name='firstname', lookup_expr='icontains', label='Student name')
    gender = ChoiceFilter(choices = GENDER, label='Gender')
    department = ChoiceFilter(choices = DEPT, label='Department')
    class Meta:
        model = Employee
        fields = ['gender', 'department']
