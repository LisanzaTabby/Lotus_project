import django_filters
from django_filters import *
from .models import Student, Employee,Donor, School

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
    STATUS = (
        ('New','New'),
        ('Contunuing','Contunuing'),
        ('Discontinued','Discontinued'),
        ('Completed','Completed'),
    )
    POSITION = (
        ('SingleOrphan', 'SingleOrphan'),
        ('DoubleOrphan', 'DoubleOrphan'),
        ('Disabled', 'Disabled'),
    )
    name = CharFilter(field_name='firstname', lookup_expr='icontains', label='Student name')
    gender = ChoiceFilter(choices = GENDER)
    levelofstudy = ChoiceFilter(choices=LEVELOFSTUDY,label='Level of Study')
    status = ChoiceFilter(choices=STATUS, label = 'Status')
    position = ChoiceFilter(choices=POSITION, label = 'Position')
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
class DonorFilter(django_filters.FilterSet):
    name = CharFilter(field_name = 'firstname', lookup_expr='icontains', label='Donor Name')
    class Meta:
        model = Donor
        fields = ['gender']

class SchoolFilter(django_filters.FilterSet):
    schoolname = CharFilter(field_name='schoolname', lookup_expr='icontains', label='School name')
    class Meta: 
        model = School
        fields = ['location']
