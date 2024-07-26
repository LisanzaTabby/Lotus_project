from .models import Student, Employee
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
