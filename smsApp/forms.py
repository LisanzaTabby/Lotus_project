from .models import Student, Employee, Donor,School
from django.forms import ModelForm

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['Date_joined']
class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        exclude = ['date_added']

class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = '__all__'
        exclude = ['date_added']